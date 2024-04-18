size = int(input('Enter the number of goal-scorers: '))
arr = []

for i in range(size):
    e = int(input(f'Score of player #{i + 1}: '))
    arr.append(e)

print('\nHighest to lowest:')
arr.sort()
arr.reverse()

for i, n in enumerate(arr):
    print(f'Player #{i + 1}: {n}')

'''
Enter the number of goal-scorers: 6
Score of player #1: 21
Score of player #2: 42
Score of player #3: 33
Score of player #4: 56
Score of player #5: 24
Score of player #6: 12

Highest to lowest:
Player #1: 56
Player #2: 42
Player #3: 33
Player #4: 24
Player #5: 21
Player #6: 12
'''