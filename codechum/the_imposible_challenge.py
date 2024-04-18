'''
---(
output: 0 -1 -3

()^--
-1 0 -2

- ( ^: decrement
+ ) v: increment
'''
symbol = input('Enter symbol: ')
x, y, z = 0, 0, 0
# ^ ( +
for i in symbol:
    if i == 'v':
        x += 1
    elif x == '^':
        x -= 1
    
    if i == ')':
        y += 1
    elif i == '(':
        y -= 1

    if i == '+':
        z += 1
    elif i == '-':
        z -= 1
    
print(x, y, z)


