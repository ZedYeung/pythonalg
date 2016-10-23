def accept_mail():
	pop_client = poplib.POP3('pop3.sina.com')
	# pop_client.set_debuglevel(1)
	pop_client.user(from_address)
	pop_client.pass_(password)
	# stat() return tuple of 2 ints (message count, mailbox size):
	print('messages count: %s & mailbox size: %s' % pop_client.stat())
	# list() return ['response', ['mesg_num octets', ...], octets]
	mails = pop_client.list()[1]
	# index start from 1
	newest_index = len(mails)
	# retr() return ['response', ['line', ...], octets]
	newest_mail = pop_client.retr(newest_index)[1]
	subject = newest_mail[35].decode('utf-8')
	subject = re.findall('Subject: (.*?)', str(newest_mail[1]), re.S)[0]
	sender = newest_mail[8][10:].decode('utf-8')
	if sender != to_address:
		pass
	else:
		if subject == "Subject: shutdown":
			return 0