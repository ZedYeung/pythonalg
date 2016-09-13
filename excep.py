
try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x/y)
except (ZeroDivisionError, TypeError, NameError):
    print('Your numbers were bogus...')
except (ZeroDivisionError, TypeError, NameError) as e:
    print(e)
x = None
try:
    x = 1/0
finally:
    print('clean')
    del x


