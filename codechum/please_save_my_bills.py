n = int(input('Enter N: '))

arr = []
for i in range(n):
    e = int(input(f'Enter item cost {i + 1}: '))
    arr.append(e)

bill = int(input('Enter bill: '))
cost = bill - sum(arr)

valid_changes = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
total = cost

changes = []
while True:
    if total >= 1000:
        changes.append(1000)
        total -= 1000
    elif total >= 500:
        changes.append(500)
        total -= 500
    elif total >= 200:
        changes.append(200)
        total -= 200
    elif total >= 100:
        changes.append(100)
        total -= 100
    elif total >= 50:
        changes.append(50)
        total -= 50
    elif total >= 20:
        changes.append(20)
        total -= 20
    elif total >= 10:
        changes.append(10)
        total -= 10
    elif total >= 5:
        changes.append(5)
        total -= 5
    elif total >= 1:
        changes.append(1)
        total -= 1
    elif total == 0:
        break

for i in range(len(valid_changes)):
    print(f'{valid_changes[i]} = {changes.count(i)}')
    