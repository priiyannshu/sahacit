import { useState } from 'react';
import { getServiceManager } from './services/jupyter';
import { NotebookView } from './components/NotebookView';
import { FileExplorer } from './components/FileExplorer';
import './App.css';

function getInitialPath(): string {
  const params = new URLSearchParams(window.location.search);
  return params.get('path') || 'test/sandbox.ipynb';
}

function App() {
  const [activePath, setActivePath] = useState<string>(getInitialPath);
  const [isSidebarOpen, setIsSidebarOpen] = useState<boolean>(true);
  const services = getServiceManager();

  const handleSelectNotebook = (newPath: string) => {
    setActivePath(newPath);
    const url = new URL(window.location.href);
    url.searchParams.set('path', newPath);
    window.history.replaceState(null, '', url.toString());
  };

  return (
    <div className="app-layout">
      <FileExplorer 
        services={services}
        activePath={activePath}
        onSelectNotebook={handleSelectNotebook}
        isOpen={isSidebarOpen}
        onToggle={() => setIsSidebarOpen(!isSidebarOpen)}
      />
      <div className={`canvas-wrapper ${isSidebarOpen ? 'with-sidebar' : 'full-width'}`}>
        <div className="canvas-content">
          <NotebookView 
            key={activePath} 
            path={activePath} 
            isSidebarOpen={isSidebarOpen}
            onToggleSidebar={() => setIsSidebarOpen(true)}
          />
        </div>
      </div>
    </div>
  );
}

export default App;

