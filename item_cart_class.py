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
        if quantity == 0:
            self.total -= price*float(self.items[itemname])
            del self.items[itemname]
            
        elif itemname in self.items:
            self.total -= (price*float(self.items[itemname]))
            self.items.update({itemname: float(quantity)})
            self.total += (float(quantity) * price)
             
                
        
