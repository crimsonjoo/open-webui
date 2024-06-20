!ldconfig -v
!nvidia-smi
import subprocess
import os

!cd open-webui/backend
print(subprocess.run(["bash start.sh"], shell=True))