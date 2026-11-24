import { useEffect, useState, useRef, useCallback } from 'react';
import { getServiceManager } from '../services/jupyter';
import { CellView } from './CellView';

interface NotebookViewProps {
  path: string;
  isSidebarOpen?: boolean;
  onToggleSidebar?: () => void;
}

export function NotebookView({ path, isSidebarOpen, onToggleSidebar }: NotebookViewProps) {
  const [cells, setCells] = useState<any[]>([]);
  const [session, setSession] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);
  const [status, setStatus] = useState<string>('Initializing...');
  const [isSaving, setIsSaving] = useState<boolean>(false);

  const serviceManagerRef = useRef<any>(null);
  const lastModifiedRef = useRef<string | null>(null);
  const isSavingRef = useRef<boolean>(false);
  const saveTimeoutRef = useRef<any>(null);
  const cellsRef = useRef<any[]>([]);

  // Keep cellsRef in sync with cells state
  const updateCellsState = (newCells: any[]) => {
    cellsRef.current = newCells;
    setCells(newCells);
  };

  const saveNotebookNow = useCallback(async (cellsToSave?: any[]) => {
    if (!serviceManagerRef.current) return;
    try {
      isSavingRef.current = true;
      setIsSaving(true);
      const targetCells = cellsToSave || cellsRef.current;
      const model = await serviceManagerRef.current.contents.get(path);
      model.content.cells = targetCells;
      const saved = await serviceManagerRef.current.contents.save(path, model);
      lastModifiedRef.current = saved.last_modified;
    } catch (err) {
      console.error('Failed to save notebook:', err);
    } finally {
      setTimeout(() => {
        isSavingRef.current = false;
        setIsSaving(false);
      }, 400);
    }
  }, [path]);

  const init = useCallback(async () => {
    setError(null);
    let intervalId: any = null;
    let localSession: any = null;

    try {
      setStatus('Connecting to Jupyter Server...');
      const services = getServiceManager();
      serviceManagerRef.current = services;
      await services.ready;

      setStatus('Loading notebook...');
      const model = await services.contents.get(path);
      lastModifiedRef.current = model.last_modified;
      updateCellsState(model.content.cells);

      setStatus('Connecting to Python kernel...');
      let existingSession: any = null;
      try {
        existingSession = await services.sessions.findByPath(path);
      } catch (e) {
        console.warn('[NotebookView] findByPath skipped, starting new session:', e);
      }

      if (existingSession) {
        localSession = services.sessions.connectTo({ model: existingSession });
      } else {
        localSession = await services.sessions.startNew({
          name: path,
          path: path,
          type: 'notebook',
          kernel: { name: 'python3' }
        });
      }

      setSession(localSession);
      setStatus('Ready');

      // Watch for file changes on disk (e.g. from jupyter-tutor or external agents)
      intervalId = setInterval(async () => {
        if (isSavingRef.current || !serviceManagerRef.current) return;
        try {
          const currentModel = await serviceManagerRef.current.contents.get(path);
          if (currentModel.last_modified !== lastModifiedRef.current) {
            console.log('[NotebookView] External change detected. Reloading cells...');
            lastModifiedRef.current = currentModel.last_modified;
            updateCellsState(currentModel.content.cells);
          }
        } catch (e) {
          console.warn('[NotebookView] Polling check error:', e);
        }
      }, 1200);

    } catch (err: any) {
      console.error('Connection error:', err);
      setError(err.message || String(err));
    }

    return () => {
      if (intervalId) clearInterval(intervalId);
      if (localSession) {
        try { localSession.dispose(); } catch (e) {}
      }
    };
  }, [path]);

  useEffect(() => {
    let cleanupPromise = init();
    return () => {
      cleanupPromise.then(cleanup => cleanup && cleanup());
      if (saveTimeoutRef.current) clearTimeout(saveTimeoutRef.current);
    };
  }, [init]);

  const updateCell = (index: number, newCellData: any) => {
    const updated = [...cellsRef.current];
    updated[index] = newCellData;
    updateCellsState(updated);

    if (saveTimeoutRef.current) clearTimeout(saveTimeoutRef.current);
    saveTimeoutRef.current = setTimeout(() => {
      saveNotebookNow(updated);
    }, 400);
  };

  const insertCell = (index: number, type: 'code' | 'markdown') => {
    const newCell = {
      cell_type: type,
      source: '',
      metadata: {},
      ...(type === 'code' ? { outputs: [], execution_count: null } : {})
    };
    const updated = [...cellsRef.current];
    updated.splice(index, 0, newCell);
    updateCellsState(updated);
    saveNotebookNow(updated);
  };

  const deleteCell = (index: number) => {
    const updated = [...cellsRef.current];
    updated.splice(index, 1);
    updateCellsState(updated);
    saveNotebookNow(updated);
  };

  const executeCell = async (index: number) => {
    if (!session || !session.kernel) return;
    const currentCells = cellsRef.current;
    const cell = currentCells[index];
    if (cell.cell_type !== 'code') return;

    if (saveTimeoutRef.current) clearTimeout(saveTimeoutRef.current);

    const runningCells = [...cellsRef.current];
    runningCells[index] = {
      ...runningCells[index],
      outputs: [],
      execution_count: '*'
    };
    updateCellsState(runningCells);

    const code = Array.isArray(cell.source) ? cell.source.join('') : cell.source;
    const future = session.kernel.requestExecute({ code });

    let latestExecutionCount: number | null = null;

    future.onIOPub = (msg: any) => {
      const msgType = msg.header.msg_type;
      const content = msg.content;
      
      const newCells = [...cellsRef.current];
      const targetCell = { ...newCells[index] };
      targetCell.outputs = targetCell.outputs ? [...targetCell.outputs] : [];

      if (msgType === 'execute_result' || msgType === 'display_data') {
        targetCell.outputs.push({
          output_type: msgType,
          data: content.data,
          metadata: content.metadata,
          execution_count: content.execution_count
        });
      } else if (msgType === 'stream') {
        targetCell.outputs.push({
          output_type: 'stream',
          name: content.name,
          text: content.text
        });
      } else if (msgType === 'error') {
        targetCell.outputs.push({
          output_type: 'error',
          ename: content.ename,
          evalue: content.evalue,
          traceback: content.traceback
        });
      }
      
      newCells[index] = targetCell;
      updateCellsState(newCells);
    };

    future.onReply = (msg: any) => {
      if (msg.content && msg.content.execution_count != null) {
        latestExecutionCount = msg.content.execution_count;
      }
    };

    try {
      await future.done;
    } catch (e) {
      console.warn('Future completed with error or interruption', e);
    }

    const finalCells = [...cellsRef.current];
    finalCells[index] = {
      ...finalCells[index],
      execution_count: latestExecutionCount ?? 1
    };
    updateCellsState(finalCells);
    await saveNotebookNow(finalCells);
  };

  if (error) {
    return (
      <div className="error-banner">
        <h3>Connection Error</h3>
        <p>{error}</p>
        <p>Ensure the Jupyter Server is running on port 8888 with token 'sahacit-dev' and root_dir pointing to 'sahacit/library'.</p>
        <button 
          type="button" 
          className="top-add-btn" 
          onClick={() => init()}
          style={{ marginTop: '12px' }}
        >
          🔄 Retry Connection
        </button>
      </div>
    );
  }

  if (!session) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>{status}</p>
      </div>
    );
  }

  return (
    <div className="notebook-view">
      <header className="notebook-header">
        <div className="header-left">
          {!isSidebarOpen && onToggleSidebar && (
            <button 
              type="button" 
              className="sidebar-toggle-header-btn"
              onClick={onToggleSidebar}
              title="Open Library Explorer"
            >
              📁 Library
            </button>
          )}
          <span className="notebook-path">{path}</span>
          <span className={`save-indicator ${isSaving ? 'saving' : 'saved'}`}>
            {isSaving ? '● Saving...' : '✓ Saved'}
          </span>
        </div>
        <div className="header-right">
          <span className="kernel-badge">● Python 3 (Kernel Connected)</span>
          <button 
            type="button" 
            className="top-add-btn" 
            onClick={() => insertCell(0, 'markdown')}
            title="Add Markdown cell at top"
          >
            + Markdown
          </button>
          <button 
            type="button" 
            className="top-add-btn" 
            onClick={() => insertCell(0, 'code')}
            title="Add Code cell at top"
          >
            + Code
          </button>
        </div>
      </header>
      
      <main className="cells-stack">
        {cells.map((cell, idx) => (
          <CellView 
            key={cell.id || idx} 
            cell={cell} 
            onChange={(newCell) => updateCell(idx, newCell)}
            onExecute={() => executeCell(idx)}
            onInsert={(type) => insertCell(idx + 1, type)}
            onDelete={() => deleteCell(idx)}
          />
        ))}
        {cells.length === 0 && (
          <div className="empty-notebook-notice">
            <p>This notebook has no cells yet.</p>
            <div className="empty-actions">
              <button type="button" onClick={() => insertCell(0, 'markdown')}>+ Add Markdown Cell</button>
              <button type="button" onClick={() => insertCell(0, 'code')}>+ Add Code Cell</button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
