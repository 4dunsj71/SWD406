#!/usr/bin/python
import sqlite3
db = sqlite3.connect('orinoco.db')
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

def _first_tuple_string(all_rows,str_out):
    first_element = []
    for a_tuple in all_rows:
        first_element.append(a_tuple[0])
    first_tuple = first_element[0]
    global str_out
    str_out = str(first_tuple)


cat_try = 'SELECT category_id,\
           category_description\
            FROM categories'

cursor = db.cursor()
cursor.execute(cat_try)

all_rows = cursor.fetchall()
str_out
_first_tuple_string(all_rows,str_out)
print(str_out)
