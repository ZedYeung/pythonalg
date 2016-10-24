import os
import sys
"""
argv[1] can be these alphabet
/l	Log off.
/s	Shutdown the computer.
/r	Shutdown and restart the computer.
/g	Shutdown and restart the computer. After the system is rebooted, restart any registered applications.
/a	Abort a system shutdown during the time-out period.
/p	Turn off the local computer with no time-out or warning.
/f	Force running applications to close without forewarning users.
argv[2] is the timeout
/t xxx	Set the time-out period before shutdown to xxx seconds.
The valid range is 0-315360000 (10 years), with a default of 30.
If the timeout period is greater than 0, the /f parameter is implied.
"""
print('wait for shutdown...')
os.system('shutdown -%s -t %s' % (sys.argv[1], sys.argv[2]))

