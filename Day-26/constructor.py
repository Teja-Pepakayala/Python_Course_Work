"""
class Instagram:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		print(f"Welcome to Instagram, {self.username}")


teja = Instagram("teja", "2333123")
sai = Instagram("sai", "sai123")
nani = Instagram("nani", "nani123")
mohan = Instagram("mohan", "mohan123")

"""

class Instagram:
	def __init__(self, username, password):
		self.username = username
		self.__password = password
		self._post = []

	def getpassword(self):
		return self.__password

	def setpassword(self, password):
		self.__password = password

	@property
	def password(self):
		return self.__password

	@property
	def accesspost(self):
		return self._post

	@accesspost.setter
	def accesspost(self, post):
		self._post = post

teja = Instagram("teja", "2333123")
print(teja.username)
print(teja.getpassword())
print(teja.accesspost)

teja.username = '2333123'
print(teja.username)

teja.setpassword('1342546768')
print(teja.getpassword)

teja.accesspost = 'py'
teja.accesspost = 'str'
teja.accesspost = 'py sst'
