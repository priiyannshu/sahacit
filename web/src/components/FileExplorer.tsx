import { useState, useEffect } from 'react';
import { ServiceManager } from '@jupyterlab/services';

interface FileItem {
  name: string;
  path: string;
  type: 'directory' | 'notebook' | 'file';
  last_modified?: string;
}

interface FileExplorerProps {
  services: ServiceManager | null;
  activePath: string;
  onSelectNotebook: (path: string) => void;
  isOpen: boolean;
  onToggle: () => void;
}

export function FileExplorer({
  services,
  activePath,
  onSelectNotebook,
  isOpen,
  onToggle
}: FileExplorerProps) {
  const [items, setItems] = useState<FileItem[]>([]);
  const [currentDir, setCurrentDir] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const fetchDirectory = async (dirPath: string = '') => {
    if (!services) return;
    try {
      setLoading(true);
      setError(null);
      const model = await services.contents.get(dirPath);
      if (model.content && Array.isArray(model.content)) {
        const sorted = [...model.content].sort((a, b) => {
          if (a.type === 'directory' && b.type !== 'directory') return -1;
          if (a.type !== 'directory' && b.type === 'directory') return 1;
          return a.name.localeCompare(b.name);
        });
        setItems(sorted);
        setCurrentDir(dirPath);
      }
    } catch (err: any) {
      console.error('Failed to list files:', err);
      setError(err.message || 'Error listing files');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (services) {
      fetchDirectory('');
    }
  }, [services]);

  const handleItemClick = (item: FileItem) => {
    if (item.type === 'directory') {
      fetchDirectory(item.path);
    } else if (item.type === 'notebook') {
      onSelectNotebook(item.path);
    }
  };

  const handleGoUp = () => {
    if (!currentDir) return;
    const parts = currentDir.split('/').filter(Boolean);
    parts.pop();
    fetchDirectory(parts.join('/'));
  };

  const handleCreateNotebook = async () => {
    if (!services) return;
    try {
      const newModel = await services.contents.newUntitled({
        path: currentDir,
        type: 'notebook'
      });
      await fetchDirectory(currentDir);
      onSelectNotebook(newModel.path);
    } catch (err: any) {
      alert(`Could not create notebook: ${err.message || err}`);
    }
  };

  if (!isOpen) {
    return (
      <div className="file-explorer-collapsed">
        <button 
          type="button" 
          className="expand-sidebar-btn" 
          onClick={onToggle}
          title="Open Library Explorer"
        >
          🏛️ <span>Library</span>
        </button>
      </div>
    );
  }

  return (
    <aside className="file-explorer">
      <div className="explorer-header">
        <div className="explorer-title">
          <span className="library-icon">🏛️</span>
          <span className="library-label">sahacit Library</span>
        </div>
        <div className="explorer-actions">
          <button 
            type="button" 
            className="action-icon-btn" 
            onClick={() => fetchDirectory(currentDir)} 
            title="Refresh library"
          >
            ↻
          </button>
          <button 
            type="button" 
            className="action-icon-btn" 
            onClick={handleCreateNotebook} 
            title="New Notebook"
          >
            +
          </button>
          <button 
            type="button" 
            className="action-icon-btn toggle-btn" 
            onClick={onToggle} 
            title="Collapse Sidebar"
          >
            ◀
          </button>
        </div>
      </div>

      <div className="current-path-bar">
        <button 
          type="button" 
          disabled={!currentDir} 
          onClick={handleGoUp} 
          className="up-btn"
          title="Go to parent folder"
        >
          ⬆
        </button>
        <span className="path-text" title={currentDir || 'library root'}>
          /{currentDir || ''}
        </span>
      </div>

      {loading && <div className="explorer-loading">Reading library...</div>}
      {error && <div className="explorer-error">{error}</div>}

      {!loading && (
        <ul className="file-list">
          {items.map((item) => {
            const isSelected = item.path === activePath;
            return (
              <li
                key={item.path}
                className={`file-item ${item.type} ${isSelected ? 'selected' : ''}`}
                onClick={() => handleItemClick(item)}
              >
                <span className="item-icon">
                  {item.type === 'directory' ? '📁' : item.type === 'notebook' ? '📓' : '📄'}
                </span>
                <span className="item-name">{item.name}</span>
              </li>
            );
          })}
          {items.length === 0 && !error && (
            <li className="empty-dir">Folder is empty</li>
          )}
        </ul>
      )}
    </aside>
  );
}
