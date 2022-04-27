#!/usr/bin/env python3

# YOU ARE NOT IN C++ LAND!!

n = int(input("Enter number of elements : "))

a = list(map(str, input("\nEnter the numbers : ").strip().split()))[:n]

for it in a:
    filename = it
    f = open(filename, 'w')

    f.write("something")
    f.close()

print("\nFiles created - ", a)
