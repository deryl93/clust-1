import os
proxy = 'http://user:pass@167.99.236.14:80'
os.system('curl ident.me')
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.system('curl ident.me')
