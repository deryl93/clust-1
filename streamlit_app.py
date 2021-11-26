import os
proxy = '36.67.63.239:38071'
os.system('curl ipinfo.io')
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.system('curl ipinfo.io')
