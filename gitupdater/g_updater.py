


# call system wide script
from sys import argv
# add a msg to the command line when calling script
print(argv[1:])
# add msg to script var to be used
msg = ''.join(argv[1:])
print(msg)

# call git add .
# once that msg is available add it to git -m "msg"
# call git push