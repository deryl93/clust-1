import os
proxy = 'https://50.233.228.147:8080'
os.system('curl ipinfo.io')
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.system('curl ipinfo.io')
