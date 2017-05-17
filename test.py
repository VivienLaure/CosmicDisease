class Premiere(object):
	discount = False
	def __init__(self, prix):
		self.prix = prix
		if self.prix < 5000:
			self.discount = True
        
c = Premiere(10000)
print(c.discount)
