import { ServerConnection, ServiceManager } from '@jupyterlab/services';

let serviceManager: ServiceManager | null = null;

export function getServiceManager(): ServiceManager {
  if (!serviceManager || serviceManager.isDisposed) {
    const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const settings = ServerConnection.makeSettings({
      baseUrl: window.location.origin,
      token: 'sahacit-dev',
      wsUrl: `${wsProtocol}//${window.location.host}`
    });
    serviceManager = new ServiceManager({ serverSettings: settings });
  }
  return serviceManager;
}
