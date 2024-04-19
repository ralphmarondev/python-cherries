'''
     **
 **********
 **********
 **********
************
'''

def print_pattern(w, h):
    # if width = odd
    if w % 2 != 0:
        mid = int(w // 2) + 1
        for i in range(h):
            if i == 0:
                print(' ' * mid + '*')
            elif i == h - 1:
                print('*' * (w + 2))
                break
            else:
                print(' ' + '*' * w + ' ')
        return
    
    # width = even
    mid = int(w // 2)
    for i in range(h):
        if i == 0:
            print(' ' * mid  + '**')
        elif i == h - 1:
            print('*' * (w + 2))
        else:
            print(' ' + '*' * w + ' ')
  

w = 10
h = 5

print_pattern(w, h)


