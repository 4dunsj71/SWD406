#question 1
print("introduction to")
print("python programming")

#question 2
print("intro to \n python programming")

#question 3
my_age = 21
print("my age is",my_age)

#question 4
my_name = "jon"
my_age = 21
my_age = my_age+1
print("next year",my_name,"will be",my_age,"years old")

#question 5
name= input("enter your name: ")
place_of_birth=input("enter your place of birth: ")
print(name,"was born in",place_of_birth)

#question 6
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))
avg = ((num1+num2+num3)/3)
print("the average of {0} , {1} and {2} is: {3}" .format(num1,num2,num3,avg))

#question 7
num = int(input("enter a number: "))
if(num%2)==0:
    print("{0} is an even number".format(num))
else:
    print("{0} is an odd number".format(num))
    
#question 8
grade = int(input("enter your grade as a percentage: "))
if grade <=40:
    print("your grade sucks, you fail")
if grade>=40 and grade<=79:
    print("you passed")
if grade>=80:
    print("distinction")
    
