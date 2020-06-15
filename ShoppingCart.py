#! /usr/bin/env python3
class ShoppingCart:
	def __init__(self):
		self._total = 0
		self._items = {}
		
	def addItem(self, item, quantity, price):
		self._total +=  quantity * price
		self._items[item] = quantity
		
	def removeItem(self, item):
		self._total -= quantity * price 
		self._items[item] = quantity
		
	def checkout(self):
		pass
		
		
Cart1 = ShoppingCart()

Cart1.addItem("broccoli", 3, 6)
print(Cart1._items)
print(Cart1._total)




	
