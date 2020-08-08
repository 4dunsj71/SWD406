#!/usr/bin/python
import sqlite3

def _display_options(all_options,title,type):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    for option in all_options:
        code = option[0]
        desc = option[1]
        print("{0}.\t{1}".format(option_num, desc))
        option_num = option_num + 1
        option_list.append(code)
    selected_option = 0
    while selected_option > len(option_list) or selected_option == 0:
        prompt = "Enter the number against the "+type+" you want to choose: "
        selected_option = int(input(prompt))
    return option_list[selected_option - 1]

db = sqlite3.connect('orinoco.db')
order_get ="SELECT IFNULL(op.order_id,'empty'), \
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

cat_get =  'SELECT product_id, \
            product_description \
            FROM products \
            WHERE category_id = (?)'

seller_get ="SELECT seller_id\
            ,price\
            FROM product_sellers\
            WHERE product_id = (?)"

loopval = 0
loopval2 = 0

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
            cursor.execute(order_get,(shopperId,))
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
                cursor.close()

            leavemenu = input("return to main menu? if you select no, the program will terminate(y/n)")
            if leavemenu == 'y':
                loopval = 0
            elif leavemenu == 'n':
                print('exiting program...')
                loopval = 1




        elif menuInput == '2':
        
            while loopval2 == 0: 
                    
                basket_input = input('select an option: \n \
                1. Mobile Phones and accessories \n \
                2. TVs and Home Cinema \n \
                3. Cameras and accessories \n \
                4. Audio and Hifi \n \
                5. Computers and accessories \n \
                5. Gaming \n    ')

                basket_val = 1
                print('   ID               product description')
                cursor.execute(cat_get,basket_input)
                all_rows = cursor.fetchall()
                for row in all_rows:
                    product_id = row[0]
                    product_description = row[1]
                    print('{0:5}\t\t{1:15}'.format(product_id,product_description))
                cursor.close()

                product_input = input('enter the product ID of the item you wish to purchase: ')
                print('seller ID\t\tprice')
                cursor = db.cursor()
                cursor.execute(seller_get,(product_input))
                all_rows=cursor.fetchall()
                for row in all_rows:
                    seller_id = row[0]
                    price = row[1]
                    print('{0}\t\t{1.2f}'.format(seller_id,price))
                cursor.close()
            leavemenu = input("return to main menu? if you select no, the program will terminate(y/n)")
            if leavemenu == 'y':
                loopval2 = 0
            elif leavemenu == 'n':
                loopval2 = 1
            

        elif menuInput == '3':
            print('')

        elif menuInput == '4':
            print('')

        elif menuInput == '5':
            loopval = 1
            print('exiting program...')

    else:
        print("entered value is not numerical, please try again")