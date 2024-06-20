!ldconfig -v
!nvidia-smi
import subprocess
import os

!pwd
!ls
!cd ./backend
print(subprocess.run(["bash start.sh"], shell=True))