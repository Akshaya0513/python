#Concatenation: Joining of two or more strings together to form a single string
str1 = "Akshaya"
str2 = "Rapolu"
final_str = str1 + str2
print (final_str)

#length of string: Finding of how many characters present in Concatenation & Spaces are also counted on these
str1 = "Akshaya"
len1 = len(str1)
print (len1)
str2 = "Rapolu"
len2 = len(str2)
print (len2)
final_str = str1 + str2
print (final_str)

#Indexing: Indexing means accessing a particular character from a string using its position (index).
str = "Akshaya Rapolu"
print(str[0])
print(str[1])

#Slicing: Extracting a part of a string.
str = "Akshaya Rapolu"
print(str[1:3])
print(str[3:11]) 
print (str[6:len(str)])

#Negative indexing: used to access characters in a string from the end.
str ="Akshaya Rapolu"
print (str[-15:-1])

##String Functions

#1. (str.endswith("")) is used to checks whether a string ends with a particular value.
str = "Akshaya Rapolu"
print (str.endswith("olu"))
print (str.endswith("Aks"))

#2.(str.capitalize()) is used to converts the first character of a string to uppercase and converts the remaining characters to lowercase.
str ="akshaya"
print (str.capitalize())

#3. (str.replace("old","new")): is used to replace a part of a string with another string.
str ="Akshaya"
print (str.replace("a","o"))
print (str.replace("Akshaya","Rapolu"))

#4.(str.find()): is used to find the position (index) of a character or substring inside a string.
str = "My name is Akshaya"
print (str.find("a"))
print (str.find("is"))

#5.(str.count()): is used to count how many times a character or substring occurs in a string.
str = "My name is Akshaya"
print (str.count("a"))


#Conditional Statements
age = int (input("Enter your age: "))
if(age<=12):
   print ("You'r child")
elif(age<=18):
   print ("You'r teenage")
elif(age<=29):
   print ("You'r Adult")
elif(age<=60):
   print ("You'r Matured")
else:
   print ("Enter valid number")

