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
    global selected_option
    selected_option = 0
    while selected_option > len(option_list) or selected_option == 0:
        prompt = "Enter the number against the "+type+" you want to choose: "
        selected_option = int(input(prompt))
    return option_list[selected_option - 1]
def _display_3_options(all_options,title,type):
    option_num = 1
    option_list = []
    print("\n",title,"\n")
    for option in all_options:
        code = option[0]
        desc = option[1]
        desc2 = option[2]
        desc3 = option[3]
        print("{0}.\t{1}\t{2}\t{3}".format(option_num, desc, desc2, desc3))
        option_num = option_num + 1
        option_list.append(code)
    global selected_option
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

cat_try = 'SELECT category_id,\
           category_description\
            FROM categories'

seller_get ="SELECT ps.product_id\
            ,s.seller_name\
            ,ps.price\
            ,s.seller_id\
            FROM product_sellers ps\
                 INNER JOIN\
            sellers s ON s.seller_id = ps.seller_id\
            WHERE product_id = (?); "
order_confirm ='SELECT ps.seller_id\
                ,s.seller_name\
                ,p.product_description\
                ,ps.price\
                FROM product_sellers ps\
                    INNER JOIN\
                sellers s ON s.seller_id = ps.seller_id\
                    INNER JOIN\
                products p ON p.product_id = ps.product_id\
                WHERE ps.product_id = ?\
                AND ps.seller_id = ?'
basket_add = 'INSERT INTO shopper_basket(shopper_id,basket_number)\
              VALUES(?,?);\
              INSERT INTO {idfk the name of the table}(basket_number,shopper_id,product_id,quantity)\
              VALUES(?,?,?);"
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
            print('Add an item to your basket\n\n')
            while loopval2 == 0:
                cursor.execute(cat_try)
                all_rows = cursor.fetchall()
                _display_options(all_rows,'categories','number')
                
                selected_category = str(selected_option)
                cursor.execute(cat_get,selected_category)
                all_rows = cursor.fetchall()
                _display_options(all_rows,'products','number')
                first_element = []
                for a_tuple in all_rows:
                    first_element.append(a_tuple[0])
                
                selected_product = ((first_element[(selected_option-1)]))
                sel_prod_id = str(selected_product)
                cursor.execute(seller_get,[sel_prod_id])
                all_rows = cursor.fetchall()
                _display_3_options(all_rows,'sellers who sell this product','number')
                first_element = []
                for a_tuple in all_rows:
                    first_element.append(a_tuple[3])
                selected_seller = ((first_element[(selected_option-1)]))
                sel_sell_id = str(selected_seller)
                print(type(sel_sell_id))
                print(type(sel_prod_id))

                cursor.execute(order_confirm,((sel_prod_id),(sel_sell_id)))
                all_rows = cursor.fetchall()
                for row in all_rows:
                    seller_id = row[0]
                    seller_name = row[1]
                    product_description =row[2]
                    price = row[3]
                    print("{0}\t{1}\t{2}\t{3}".format(seller_id,seller_name,product_description,price))
                buy_shit = input("enter a quantity to buy: ")
                if buy_shit.isdigit:
                    if (confirm = input("confirm action (y/n): ") = y):
                        cursor.execute(basket_add,(shopper_id,sel_pod_id,basket_number,buy_shit))
                    
                else:
                    print("that was not a number, try again")
                
                        
                        
                

            

        elif menuInput == '3':
            print('')

        elif menuInput == '4':
            print('')

        elif menuInput == '5':
            loopval = 1
            print('exiting program...')

    else:
        print("entered value is not numerical, please try again")