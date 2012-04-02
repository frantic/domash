import base64
import time

time.sleep(1)
print base64.b64decode('SGFwcHkgYmlydGhkYXksIERvbWFzaCEgWW91IGFyZSBsZWdlbmQuLi4=')
time.sleep(1)
for i in xrange(5):
	print '.'
	time.sleep(0.5)
print base64.b64decode('Li4uZGFyeSE=')
