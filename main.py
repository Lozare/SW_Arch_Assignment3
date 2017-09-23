from item_cart_class import Item
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

    
    

def main():
    dbConnection = createDbConnection("assignment3.db")
    inventory = buildInventory(dbConnection)
    
main()    
