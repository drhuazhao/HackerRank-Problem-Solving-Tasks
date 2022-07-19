#!/bin/python3
class Book():
	frontsize = 9
	Pagewidth = 15
	def __init__(self, name, writer, length):
		self.name = name
		self.writer = writer
		self.length = length
		
		
Book1 = Book("Legendary Iwata", "Iwata", 5000)
print(Book1.name)
print("Book's front size: "+ str(Book1.frontsize))