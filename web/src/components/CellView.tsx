import { useState, useEffect, useMemo } from 'react';
import CodeMirror, { keymap } from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { markdown } from '@codemirror/lang-markdown';
import { EditorView } from '@codemirror/view';
import Markdown from 'react-markdown';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import 'katex/dist/katex.min.css';
import Convert from 'ansi-to-html';

const convert = new Convert({ escapeXML: true });

interface CellViewProps {
  cell: any;
  onChange: (cell: any) => void;
  onExecute: () => void;
  onInsert: (type: 'code' | 'markdown') => void;
  onDelete: () => void;
}

export function CellView({ cell, onChange, onExecute, onInsert, onDelete }: CellViewProps) {
  const [source, setSource] = useState(Array.isArray(cell.source) ? cell.source.join('') : (cell.source || ''));
  // If it is an empty markdown cell (e.g. newly created), open in edit mode; otherwise, render cleanly
  const [isEditing, setIsEditing] = useState(() => {
    if (cell.cell_type !== 'markdown') return false;
    const initialText = Array.isArray(cell.source) ? cell.source.join('') : (cell.source || '');
    return initialText.trim().length === 0;
  });

  useEffect(() => {
    setSource(Array.isArray(cell.source) ? cell.source.join('') : (cell.source || ''));
  }, [cell.source]);

  const isRunning = cell.execution_count === '*';

  // Prevent Shift-Enter newline jump inside CodeMirror for code execution
  const codeKeymap = useMemo(() => {
    return keymap.of([
      {
        key: 'Shift-Enter',
        run: (view) => {
          const currentText = view.state.doc.toString();
          setSource(currentText);
          onChange({ ...cell, source: currentText });
          onExecute();
          return true;
        },
      },
    ]);
  }, [cell, onChange, onExecute]);

  // Markdown editor keymap: Shift-Enter saves and exits edit mode
  const markdownKeymap = useMemo(() => {
    return keymap.of([
      {
        key: 'Shift-Enter',
        run: (view) => {
          const currentText = view.state.doc.toString();
          setSource(currentText);
          onChange({ ...cell, source: currentText });
          setIsEditing(false);
          return true;
        },
      },
      {
        key: 'Escape',
        run: (view) => {
          const currentText = view.state.doc.toString();
          setSource(currentText);
          onChange({ ...cell, source: currentText });
          setIsEditing(false);
          return true;
        },
      },
    ]);
  }, [cell, onChange]);

  const handleSourceChange = (val: string) => {
    setSource(val);
    onChange({ ...cell, source: val });
  };

  const handleBlur = () => {
    onChange({ ...cell, source });
  };

  const handleRunClick = (e: React.MouseEvent) => {
    e.stopPropagation();
    onChange({ ...cell, source });
    onExecute();
  };

  const handleToggleMarkdownEdit = () => {
    if (isEditing) {
      onChange({ ...cell, source });
      setIsEditing(false);
    } else {
      setIsEditing(true);
    }
  };

  const renderOutput = (output: any, idx: number) => {
    if (output.output_type === 'stream') {
      return <pre key={idx} className="output-stream">{output.text}</pre>;
    } else if (output.output_type === 'execute_result' || output.output_type === 'display_data') {
      const data = output.data;
      if (data['text/html']) {
        return <div key={idx} dangerouslySetInnerHTML={{ __html: data['text/html'] }} />;
      }
      if (data['image/png']) {
        return <img key={idx} src={`data:image/png;base64,${data['image/png'].replace(/\n/g, '')}`} alt="output" />;
      }
      if (data['text/plain']) {
        return <pre key={idx} className="output-stream">{data['text/plain']}</pre>;
      }
    } else if (output.output_type === 'error') {
      const traceback = Array.isArray(output.traceback) ? output.traceback.join('\n') : (output.traceback || '');
      const htmlTraceback = convert.toHtml(traceback);
      return <pre key={idx} className="output-error" dangerouslySetInnerHTML={{ __html: htmlTraceback }} />;
    }
    return null;
  };

  return (
    <div className={`cell-container ${cell.cell_type === 'markdown' ? 'markdown-cell' : 'code-cell'}`}>
      <div className="cell-controls">
        {cell.cell_type === 'markdown' && (
          <button 
            type="button"
            className="control-btn toggle-view-btn"
            onClick={handleToggleMarkdownEdit}
            title={isEditing ? 'Save and render (Shift+Enter)' : 'Edit markdown (or double click)'}
          >
            {isEditing ? '✓ Done' : '✏️ Edit'}
          </button>
        )}
        <button type="button" className="control-btn" onClick={() => onInsert('code')}>+ Code</button>
        <button type="button" className="control-btn" onClick={() => onInsert('markdown')}>+ Text</button>
        <button type="button" className="control-btn delete-btn" onClick={onDelete} title="Delete cell">✕</button>
      </div>

      {cell.cell_type === 'code' ? (
        <div className="code-cell-layout">
          <div className="cell-execution-gutter">
            <button
              type="button"
              className={`colab-run-button ${isRunning ? 'running' : ''}`}
              onClick={handleRunClick}
              title={isRunning ? 'Executing...' : 'Run cell (Shift+Enter)'}
            >
              {isRunning ? (
                <div className="colab-spinner" />
              ) : (
                <>
                  <span className="run-icon">▶</span>
                  <span className="execution-number">
                    [{cell.execution_count != null ? cell.execution_count : ' '}]
                  </span>
                </>
              )}
            </button>
          </div>
          <div className="cell-editor-container">
            <div className="cell-editor code">
              <CodeMirror
                value={source}
                onChange={handleSourceChange}
                onBlur={handleBlur}
                extensions={[python(), codeKeymap, EditorView.lineWrapping]}
                basicSetup={{ lineNumbers: true }}
              />
            </div>
            {cell.outputs && cell.outputs.length > 0 && (
              <div className="cell-outputs">
                {cell.outputs.map((out: any, idx: number) => renderOutput(out, idx))}
              </div>
            )}
          </div>
        </div>
      ) : isEditing ? (
        <div className="markdown-cell-editing">
          <CodeMirror
            value={source}
            onChange={handleSourceChange}
            onBlur={handleBlur}
            extensions={[markdown(), markdownKeymap, EditorView.lineWrapping]}
            basicSetup={{ lineNumbers: false, foldGutter: false }}
            autoFocus
          />
          <div className="editor-footer-hint">
            Press <kbd>Shift</kbd>+<kbd>Enter</kbd> or click <strong>Done</strong> to render
          </div>
        </div>
      ) : (
        <div 
          className="markdown-render-view"
          onDoubleClick={() => setIsEditing(true)}
          title="Double-click to edit"
        >
          <div className="markdown-render">
            <Markdown remarkPlugins={[remarkMath, remarkGfm]} rehypePlugins={[rehypeKatex]}>
              {source || '*Empty markdown cell. Double click or click Edit to write.*'}
            </Markdown>
          </div>
        </div>
      )}
    </div>
  );
}
