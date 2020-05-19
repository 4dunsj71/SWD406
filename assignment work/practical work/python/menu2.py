import sqlite3

word = input("enter a word: ")
for count in range(0, len(word)):
    print("index",count,":",word[count])
    