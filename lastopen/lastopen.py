import os.path
from datetime import datetime
 
t = os.path.getatime('example.py')
 
print(datetime.fromtimestamp(t))
