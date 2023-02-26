import os
import subprocess

# Set the proxy server and port
proxy_server = '159.22.1.0' 
proxy_port = 'aaa'

# Set the program you want to open with the proxy
program_to_open = 'SETUP.exe'

# Set the arguments for the program
program_args = ['arg1', 'arg2']

# Set the environment variable for the proxy
os.environ['http_proxy'] = f'http://{proxy_server}:{proxy_port}'

# Use subprocess to open the program with the specified arguments
subprocess.Popen([program_to_open])
