import subprocess
import os
proxies = {
    'https': 'https://52.182.8.192:3128'
}

file_path = r'SETUP.exe'
env = {**proxies, **os.environ}
subprocess.Popen(file_path, env=env)
print('File opened successfully')