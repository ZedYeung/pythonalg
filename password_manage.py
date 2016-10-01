#! python
# pw.py - copy and paste password program
import sys
import pyperclip

passwords = {}
if len(sys.argv) < 2:
    print('Usage: ')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for' + account + 'copied to clipboard')
else:
    print('There is no account name' + account)
