#!/usr/bin/python
import sqlite3

db = sqlite3.connect('orinoco.db')
sql_query ="SELECT IFNULL(op.order_id,'empty'), \
            STRFTIME('%d-%m-%Y',so.order_date),\
            p.product_description,\
            s.seller_name,\
            op.price,\
            op.quantity,\
            so.order_status\
            FROM ordered_products op \
            INNER JOIN\
            shopper_orders so ON op.order_id = so.order_id\
            INNER JOIN\
            products p ON op.product_id = p.product_id\
            INNER JOIN\
            sellers s ON s.seller_id = op.seller_id\
            WHERE shopper_id = (?)\
            ORDER BY so.order_date DESC"
loopval = 0

print ("\n")
while loopval == 0:
    cursor = db.cursor()
    shopperId = input("enter your shopper ID number: ")
    if shopperId.isdigit():
        print('ORINOCO - SHOPPER MAIN MENU\n _______________________________________________ \n 1.Display your order history \
             \n 2.add an item to your basket \
              \n 3.view your basket \n 4.checkout \n 5.exit')
        menuInput = input('select an option:')
        if menuInput == '1':
            cursor = db.cursor()
            cursor.execute(sql_query,(shopperId,))
            result = all_rows = cursor.fetchall()
            data = cursor.fetchone()
            print('ORDER HISTORY \n _______________________________________________')
            print("     order ID   order date        product                 seller         price       quantity  order status\n")
            for row in all_rows:
                order_id = row[0]
                order_date = row[1]
                product_description = row[2]
                seller_name = row[3]
                price = row [4]
                quantity = row[5]
                order_status = row[6]
                print("{0:12}\t{1:}\t{2:18}\t{3:14}\t£{4:7.2f}\t{5:2}\t{6:12}".format(order_id, order_date[:10], product_description[:15], seller_name[:14], price, \
                quantity, order_status[:8]))
                if cursor.fetchone() == None:
                    print('no orders found for the provided shopper ID')

            leavemenu = input("return to main menu? if you select no, the program will terminate(y/n)")
            if leavemenu == 'y':
                loopval = 0
            elif leavemenu == 'n':
                print('exiting program...')
                loopval = 1
        elif menuInput == '2':
            print('')

        elif menuInput == '3':
            print('')

        elif menuInput == '4':
            print('')

        elif menuInput == '5':
            loopval = 1
            print('exiting program...')

    else:
        print("entered value is not numerical, please try again")