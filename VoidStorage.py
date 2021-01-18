import hashlib
import random
import string

def md5(string):
	return hashlib.md5(str(string).encode('utf-8')).hexdigest().upper()

def sha256(string):
	return hashlib.sha256(str(string).encode('utf-8')).hexdigest().upper()

def randomString(length, seed):
	random.seed(seed)
	source = string.ascii_letters + string.digits
	return ''.join((random.choice(source) for i in range(length)))


class voidStorage:
	def __init__(self, user, password):
		self.user = user.lower()
		self.password = password
		self.key = sha256(self.user + self.password)

	def findPassword(self, domain, username):
		return randomString(8, self.key + sha256(md5(domain.lower()) + md5(username.lower())))

if __name__ == '__main__':
	storage = voidStorage("", "")
	password = storage.findPassword("", "")
	print(f"Test seed password: {password}, should've been: zOiKWNZC")
	if password == "zOiKWNZC": print("Test passed, everything's great")
	else: print("Something's wrong, I can feel it") 