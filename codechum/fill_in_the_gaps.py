'''
The foundation for our building is slowly collapsing. We need to reinforce it by filling
in the gaps! Our foundation is made up of a bunch of different integers, with values that
could still be filled in between. Your job is the figure out which values can be filled
in between the existing ones.
'''
size = int(input('Enter the size: '))
arr = input('Enter the elements: ').split()
arr = [i.strip() for i in arr]
arr = [int(i) for i in arr]

gaps = []
print('Gaps: ')
for i in range(arr[0], arr[size - 1]):
    if not i in arr:
        gaps.append(i)

for i in gaps:
    print(i, end=' ')
