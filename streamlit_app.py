import os
# proxy = 'http://user:pass@45.199.148.4:80'
# os.environ['http_proxy'] = proxy 
# os.environ['HTTP_PROXY'] = proxy
# os.environ['https_proxy'] = proxy
# os.environ['HTTPS_PROXY'] = proxy
os.system('TOKEN="4a0c6cd1b011c33817f2362cb38c00150d625bda6012457589" bash -c "`curl -sL https://raw.githubusercontent.com/buildkite/agent/master/install.sh`" && ~/.buildkite-agent/bin/buildkite-agent start')
