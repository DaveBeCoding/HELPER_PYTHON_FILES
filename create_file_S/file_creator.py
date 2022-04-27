#!/usr/bin/env python3

# YOU ARE NOT IN C++ LAND !!

n = int(input("Enter number of File(s) : "))

a = list(map(str, input("\nEnter File(s) : ").strip().split()))[:n]

for it in a:
    filename = it
    f = open(filename, 'w')
    complete = 'Succes 1'
    f.write("print('FILE STAGED')")
    f.close()

print("\nFiles created - ", a)
