class Item(object):
    def __init__(self,itemname,itemprice,itemcategory,itemquantity, subcategories):
        self.name = itemname
        self.price = itemprice
        self.category = itemcategory
        self.quantity = itemquantity
        self.subcategories = subcategories

    def GetItemName(self):
        return self.name

    def GetItemPrice(self):
        return self.price

    def GetItemCategory(self):
        return self.category

    def GetItemQuantity(self):
        return self.quantity
    
    def getSubcategories(self):
        return self.subcategories

class ShoppingCart(object):      
    
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, itemname, price, quantity):
        self.total += (quantity * price)
        self.items.update({itemname: quantity})

    def remove_item(self, itemname, price, quantity):
        if itemname in self.items:
            if quantity < self.items[itemname] and quantity > 0:
                self.items[itemname].update -= quantity
                self.total -= price*quantity
                
        if quantity >= self.items[itemname]:
            self.total -= price*self.items[itemname]
            del self.items[itemname]
