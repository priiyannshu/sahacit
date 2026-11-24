c = get_config()
c.ServerApp.ip = '127.0.0.1'
c.ServerApp.port = 8888
c.ServerApp.allow_origin = 'http://localhost:5173'
c.ServerApp.allow_credentials = True
c.ServerApp.token = 'sahacit-dev'
c.ServerApp.root_dir = '/home/deadpool/omniverse/sahacit/library'
c.ServerApp.disable_check_xsrf = True
