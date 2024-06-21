import subprocess
import os

commands = [
    "ldconfig -v",
    "nvidia-smi",
    "pwd",
    "ls",
    "bash start.sh"
]

# backend 디렉토리로 변경
backend_dir = os.path.join(os.getcwd(), 'backend')

for command in commands:
    if command == "bash start.sh":
        result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=backend_dir)
    else:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    print(result.stdout)
    print(result.stderr)
    if result.returncode != 0:
        print(f"Command failed with return code {result.returncode}: {command}")
        break
