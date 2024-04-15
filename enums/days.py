from enum import Enum


class Days(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


if __name__ == '__main__':
    today = Days.TUESDAY

    if today == Days.MONDAY:
        print('Yay! It\'s Monday!')
    elif today == Days.TUESDAY:
        print('Tuesme pls pls pls mwehehehe')
    elif today == Days.WEDNESDAY:
        print('It\'s wednesday.')
    elif today == Days.THURSDAY:
        print('Oh, it\'s thursday')
    elif today == Days.FRIDAY:
        print('Today is fri-yay')
    elif today == Days.SATURDAY:
        print('Can sleep all day')
    elif today == Days.SUNDAY:
        print('Attend mass today!')
    else:
        print('Unknown day')
