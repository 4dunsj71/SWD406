
import sqlite3
#declaring location of database
db = sqlite3.connect('H:/documents/other applications/SQLiteStudio/orinoco.db')
cursor = db.cursor()
#prompting user for shopper id
shopper_id = input("Enter Your Shopper ID: ")
