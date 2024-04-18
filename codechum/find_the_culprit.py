row = int(input('Enter # of rows: '))
col = int(input('Enter # of columns: '))

print('Elements')
arr = []

for i in range(row):
    e = input('').split()
    e = [int(c) for c in e]
    arr.append(e)

culprit = int(input('Enter the culprit value: '))
found = True
for i, row in enumerate(arr):
    if found:
        for j, num in enumerate(row):
            if num == culprit:
                print(f'Culprit position: {i}, {j}')
                found = False
                break
    else:
        break

'''
Enter # of rows: 4
Enter # of columns: 4
Elements
1 4 2 3
9 1 2 3
4 2 1 1
9 2 8 3
Enter the culprit value: 8
Culprit position: 3, 2
'''