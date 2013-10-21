from datetime import date
from random import random

# You will get it, just continue
MAX_NUMBER = 100000000

pass_list = []
tries = 0

while len(pass_list) < 10:
    # Our 8-digit pass candidate
    number = str(int(random() * MAX_NUMBER))

    if len(number) != 8:
        continue

    year = int(number[4:8])
    month = int(number[2:4])
    day = int(number[:2])

    tries = tries + 1

    try:
        # try to convert our "pass" into a date
        date(year, month, day)
    except ValueError:
        # if is NOT a date (i.e, exception raised) and all numbers are distinct, proceed
        # if you aren't too paranoid, just
        if len(set(number)) == 8:
            pass_list.append(number)

for p in pass_list:
    print p

# If you are really freak, have fun:
#print 'OMG! {} iterations and only {} passes!'.format(tries, len(pass_list))