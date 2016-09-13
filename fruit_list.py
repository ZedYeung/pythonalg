width = int(input('Please enter width:'))
price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
list_format = '%-*s%*.2f'

print('=' * width)
print(header_format % (item_width, 'Ttem', price_width, 'Price'))
print('-' * width)
print(list_format % (item_width, 'Apples', price_width, 5.2))
print(list_format % (item_width, 'Pears', price_width, 4.2))
print(list_format % (item_width, 'Peach', price_width, 4.5))
print(list_format % (item_width, 'Strawberry', price_width, 8.8))
print(list_format % (item_width, 'Banana', price_width, 1))
print('=' * width)
