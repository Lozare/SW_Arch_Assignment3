from item_cart_class import Item
import item_cart_class
from item_cart_class import ShoppingCart
import sqlite3
from sqlite3 import Error
def editQuantityInInventoryDb(dbConnection,item,newQuantity):
    dbCursor = dbConnection.cursor()
    dbCursor.execute("update inventory set numberInStock = '"+str(newQuantity)+
                     "' where item = '"+item+"';")
    return

def createDbConnection(dbFile):
    try:
        connection = sqlite3.connect(dbFile)
        return connection
    except Error as e:
        print(e)
        return

def buildInventory(dbConnection):
    inventory = []
    dbCursor = dbConnection.cursor()
    dbCursor.execute("SELECT item FROM inventory ;")
    rows = dbCursor.fetchall()
    for row in rows:
        item = buildItem(dbConnection,row[0])
        inventory.append(item)
    return inventory

def buildItem(dbConnection,name):
    dbCursor = dbConnection.cursor()

    dbCursor.execute("SELECT type FROM inventory WHERE item = '"+name+"';")
    rows = dbCursor.fetchall()
    category = rows[0][0]
    
    dbCursor.execute("SELECT numberInStock from inventory where item = '"+name+"';")
    rows = dbCursor.fetchall()
    quantity = rows[0][0]

    dbCursor.execute("SELECT price from inventory where item = '"+name+"';")
    rows = dbCursor.fetchall()
    price = rows[0][0]

    subcategories={}
    dbCursor.execute("SELECT subcategory from subcategories where category = '"+
                     category+"';")
    rows = dbCursor.fetchall()
    for row in rows:
        dbCursor.execute("SELECT value from itemSubcategories where item = '"+
                         name+"' and subcategory = '"+row[0]+"';")
        rows2 = dbCursor.fetchall()
        subcategories[row[0]]=rows2[0][0]

    item = Item(name,price,category,quantity,subcategories)
    return item

def ShowCategories():
    dbConnection = createDbConnection("assignment3.db")
    dbCursor = dbConnection.cursor()
    mycart = ShoppingCart()
    print "1 - household items\n2 - books\n3 - toys\n4 - small electronics\n5 - clothes"
    choice = raw_input("Enter the number for your choice: ")

    if choice == "1":
        print "Subcategories of household items\nRooms:\n1 - bathroom"

        choice = raw_input("Enter the number for your choice: ")
        dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='bathroom'")
        print dbCursor.fetchall()

        dbCursor.execute("SELECT price FROM inventory WHERE item='toothpaste' OR item='toilet paper' ORDER BY item DESC")
        print dbCursor.fetchall()

        choice = raw_input("Enter the name of the item to add it to your cart: ")
        if choice == "toothpaste":
            choice = raw_input("Enter the quantity desired: ")
            mycart.add_item('toothpaste', 2.50, float(choice))
            print mycart.total

        if choice == "toilet paper":
            choice = raw_input("Enter the quantity desired: ")
            mycart.add_item('toilet paper', 1.99, float(choice))
            print mycart.total

    elif choice == "2":
        print "Subcategories of books\nAuthors:\n1 - Byron Williams\nISBN:\n2 - 0123456789123"

        choice = raw_input("Enter the number for your choice: ")
        if choice == "1":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='Byron Williams'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='SW Design Book'")
            print dbCursor.fetchall()

            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "SW Design Book":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('SW Design Book', 99.99, float(choice))
                print mycart.total

        elif choice == "2":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='0123456789123'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='SW Design Book'")
            print dbCursor.fetchall()

            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "SW Design Book":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('SW Design Book', 99.99, float(choice))
                print mycart.total
            
            
    elif choice == "3":
        print "Subcategories of toys\nAge Range:\n1 - 4-7\n2 - 8-10\nisActionFigure:\n3 - yes"
        
        choice = raw_input("Enter the number for your choice: ")
        if choice == "1":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='4-7'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='doll'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "doll":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('doll', 9.99, float(choice))
                print mycart.total

        if choice == "2":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='8-10'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='Spiderman Figure'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "Spiderman Figure":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('Spiderman Figure', 9.99, float(choice))
                print mycart.total
                
        if choice == "3":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='isActionFigure'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='Spiderman Figure'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "Spiderman Figure":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('Spiderman Figure', 9.99, float(choice))
                print mycart.total
            
    elif choice == "4":
        print "Subcategories of small electronics\nBrands:\n1 - Samsung\n2 - Apple\nDevices:\n3 - phones\n4 - cameras"

        choice = raw_input("Enter the number for your choice: ")
        if choice == "1":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='samsung'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='camera'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "camera":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('camera', 9.99, float(choice))
                print mycart.total

        if choice == "2":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='apple'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='mobile phone'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "mobile phone":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('mobile phone', 599.99, float(choice))
                print mycart.total

        if choice == "3":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='phones'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='mobile phone'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "mobile phone":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('mobile phone', 599.99, float(choice))
                print mycart.total

        if choice == "4":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='camera'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='camera'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "camera":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('camera', 9.99, float(choice))
                print mycart.total
                
    elif choice == "5":
        print "Subcategories of clothes\nGender:\n1 - Women\nSection:\n2 - Tops"

        choice = raw_input("Enter the number for your choice: ")
        if choice == "1":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='women'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='shirt'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "shirt":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('shirt', 19.99, float(choice))
                print mycart.total

        if choice == "2":
            dbCursor.execute("SELECT item FROM itemSubcategories WHERE value='tops'")
            print dbCursor.fetchall()

            dbCursor.execute("SELECT price FROM inventory WHERE item='shirt'")
            print dbCursor.fetchall()
            
            choice = raw_input("Enter the name of the item to add it to your cart: ")
            if choice == "shirt":
                choice = raw_input("Enter the quantity desired: ")
                mycart.add_item('shirt', 19.99, float(choice))
                print mycart.total
        
def main():
    dbConnection = createDbConnection("assignment3.db")
    inventory = buildInventory(dbConnection)
    ShowCategories()
    
    
    
main()    