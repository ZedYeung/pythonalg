from random import shuffle
from pprint import pprint
values = list(range(2, 11)) + 'A J Q K'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (value, suit) for value in values for suit in suits]
shuffle(deck)

# 回车发牌
#while deck:
#   input(deck.pop())
# stupid print:wait for revising
# 一次每人发13张
# each player have their own deck list and then pop and append in turn
print('deck of player1')
first = pprint(deck[:13])
print('deck of player2')
second = pprint(deck[13:26])
print('deck of player3')
third = pprint(deck[26:39])
print('deck of player4')
forth = pprint(deck[39:52])

