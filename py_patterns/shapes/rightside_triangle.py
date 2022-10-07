n = 5

for rows in range(n):
    for columns in range(rows, n):
        print('', end=' ')
    for columns in range(rows+1):
        print('*', end='')
    print()
