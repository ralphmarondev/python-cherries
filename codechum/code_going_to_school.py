row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of columns: '))
arr = [
    ['x','*','*','/'],
    ['x','*','x','x'],
    ['x','*','x','x'],
    ['o','*','x','x']
]

print('Enter the map:')
# for i in range(row):
#     e = input('').split()
#     arr.append(e)

'''
o = start
/ = stop
* = step that can be taken
x = wall cannot step
'''
temp = []
for i, row in enumerate(arr):
    for j, val in enumerate(row):
        if val == 'o':
            temp.append(i)
            temp.append(j)

start_row = temp[0]
start_col = temp[1]
print(temp)

