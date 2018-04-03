# author : kip-s
# 2017-05-02

import sys

if (len(sys.argv) != 2):
    print ('usage: $ python', sys.argv[0], 'number')
    quit()

for n in range(1, int(sys.argv[1])+1):
    if n % 3 == 0:
        print ('fizz', end='')
    if n % 5 == 0:
        print ('buzz', end='')
    elif n % 3 != 0:
        print (n, end='')
    print ()
