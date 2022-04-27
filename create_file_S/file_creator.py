#!/usr/bin/python

import sys

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))


# main.py

if __name__ == "__main__":
    # print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        if sys.argv[0] == arg:
            continue  # turn this into function -> DRIP
        else:
            print(f"Argument {i:>6}: {arg}")
            i = 1
            arrg_list = ['a', 'b', 'c', 'e', 'f']
            # arrg_list =[]
            # arrg_list.append(sys.argv)
            # print(f'THIS IS LIST {arrg_list}')
            for it in arrg_list:
                i_str = str(i)
                filename = i_str+'.txt'
                # if sys.argv[0] == arg:
                #     continue
                f = open(filename, 'w')

                f.write("something")
                f.close()
                i = i+1

# SAMPLE INPUT : python file_creator.py  test-01 test-o2 test-03.py test-04 test-5 test-06.c

# i=1
# arrg_list =['a','b','c','e','f']
# for it in arrg_list :
#  i_str=str(i)
#  filename=i_str+'.txt'
#  f=open( filename,'w')

#  f.write("something")
#  f.close()
#  i=i+1
