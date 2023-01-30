'''

The os module in Python to list the files in the current directory and then use the open() function to open and edit them. 
Here is an example of how you can use this to edit all the text files in the current directory:

'''

import os

for filename in os.listdir():
    if filename.endswith('.txt'):
        with open(filename, 'r') as f:
            lines = f.readlines()
        # Modify the lines here
        with open(filename, 'w') as f:
            f.writelines(lines)


'''




'''
