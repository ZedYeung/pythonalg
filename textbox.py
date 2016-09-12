sentence = input("Please input sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
margin_width = (screen_width - box_width)//2
print()
print(' ' * margin_width + '+' + '-' * (box_width-2) + '+')
print(' ' * margin_width + '|  ' + ' ' * text_width + '  |')
print(' ' * margin_width + '|  ' + sentence + '  |')
print(' ' * margin_width + '|  ' + ' ' * text_width + '  |')
print(' ' * margin_width + '+' + '-' * (box_width-2) + '+')
print()


