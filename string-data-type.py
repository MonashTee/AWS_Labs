myString = "This is a string"
print (myString)
print (type(myString))
print(myString + " is of the data type " + str(type(myString)))

#working with string concatenation.
firstString = "Water"
secondString = "Fall"
thirdString = firstString + secondString
print(thirdString)

FirstName = "Tehillah"
SecondName = "Ojo"
FullName = FirstName + " " + SecondName
print (FullName)

#Working with input string.
name = input("What is your name?")

#Formatting output strings
colour = input("what is your favourite colour? ")
animal = input("what is your favourite animal? ")
print("{}, you like a {} {}!".format(name,colour,animal))
