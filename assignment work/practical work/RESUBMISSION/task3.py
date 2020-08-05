#!/usr/bin/python
import sqlite3
from sqlite3 import Error


def create_connection(orinoco):
    """ create a database connection """
    conn = None
    try:
        conn = sqlite3.connect('orinoco.db')
        print("connection succeeded")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__=='__main__':
    create_connection(r"orinoco.db")
        


shopperId = input("enter your shopper ID number: ")
loopval = 0
print ("\n")
while loopval == 0:
    if num.isdigit():

        menuInput = input()



        print('ORINOCO - SHOPPER MAIN MENU\n _______________________________________________ \n 1.Display your order history \n 2.add an item to your basket \n 3.view your basket \n 4.checkout \n 5.exit')

        if menuInput == '1':
            print('ORDER HISTORY \n _______________________________________________')
            cursor.execute(sql [SELECT order_id ,delivery_address_id,payment_card_id, order_date,order_status FROM shopper_order WHERE shopper_id = (?)] shopperId )

        elif menuInput == '2':
            print('')

        elif menuInput == '3':
            print('')

        elif menuInput == '4':
            print('')

        elif menuInput == '5':
            print('')

    else:
        print("entered value is not numerical, please try again")