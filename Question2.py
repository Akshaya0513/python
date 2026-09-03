
#Question no: 1
#Finding length of your name
name = (input ("Enter your name: "))
print ("length of your name",len(name))

#Question no: 2
#Counting how many how many "$" symbol character present
sentence = (input("Enter your sentence: "))
print (sentence.count("$"))

#Question no: 3
#Checking the even or odd numbers
number = int (input("Enter the number: "))
if(number%2==0):
    print("the number is even")
else:
    print("the number is odd")

#Question no: 4
#Find which is greater number
a =int (input("Enter the number a: "))
b =int (input("Enter the number b: "))
c =int (input ("Enter the number c: "))
if (a>b and a>c):
    print ("a is greater")
elif (b>a and b>a):
    print ("b is greater")
elif (c>a and c>b):
    print ("c is greater")
else:
    print ("Invalid number")

#Question no: 5
#Checking enter the number is multiply of that entered number
number =int (input("Enter the number: "))
if(number%2==0):
    print("Multiply")
else:
    print("Not multiply")
