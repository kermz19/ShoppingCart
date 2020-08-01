#! /usr/bin/env python3
class Inventory:
	#list of items and quantities in stock
	def __init__(self, itemsInInventory = {}):
		self.itemsIninventory = itemsInInventory
		#item
		#quantity
		#price
		
		
	
class ShoppingCart:
	def __init__(self):
		self._total = 0
		self._items = {}
		
	def addItem(self, item, quantity, price):
		self._total += quantity * price
		self._items[item] = quantity
		
	def removeItem(self, item, price):
		self._total -= price
		self._items[item] -= 1
		
	def checkout(self, payment):
		if payment < self._total:
			print("Need More Cash")
		else:
			change = payment - self._total
			print("Please collect your change: ${}".format(change))
		
		
Cart1 = ShoppingCart()

Cart1.addItem("broccoli", 3, 6)
print(Cart1._items)
Cart1.removeItem("broccoli" , 6)
print(Cart1._total)
Cart1.checkout(20)


