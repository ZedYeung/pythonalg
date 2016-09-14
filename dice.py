from random import randrange             #  1
                                         #  2
num = int(input('How many dice?'))       #  3
sides = int(input('How many sides per dice?')) #  4
sum = 0                                  #  5
for i in range(num):                     #  6
    sum += randrange(sides) + 1          #  7
print('The result is', sum)              #  8
