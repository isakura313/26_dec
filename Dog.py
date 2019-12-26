class Dog:
	def __init__(self, name, weight, age):
		self.name = name
		self.weight = weight
		self.age = age
		
	def feed(self, weight):
		print("я поела Чаппи")
		self.weight = weight+1
		pass
	def bark(self):
		print("woow")
		pass
	pass

sharick = Dog("sharick", 27, 3)

sharick.feed()
print(sharick.weight)
sharick.bark()



