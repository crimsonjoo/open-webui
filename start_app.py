!ldconfig -v
!nvidia-smi
import subprocess
import os
print(subprocess.run(["bash start.sh"], shell=True))