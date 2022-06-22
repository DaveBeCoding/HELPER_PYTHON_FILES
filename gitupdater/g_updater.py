# call system wide script
from sys import argv
import subprocess
import os

# add a msg to the command line when calling script <-
# add msg to script var to be used <-
msg = ''.join(argv[1:])

# call git add . <-
os.system("git add .")

# once that msg is available add it to git -m "msg" <-
# need bytes for double quotes, pure python <-

# call git push <-