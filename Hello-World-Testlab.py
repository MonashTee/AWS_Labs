print ("Hello World")
print ("x", "10")
print ("cat")
print("Python has three numeric types: int, float, and complex")
myValue= 1 
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=3.14
print(myValue)
print(str(myValue) + " is of the data type " + str(type(myValue)))
#complex data
myValue=5j
print(myValue)
print(str(myValue) + " is of the data type " + str(type(myValue)))
#bool
myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
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

#Defining a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing list by position.
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList[2] = "orange"
print(myFruitList)

#Defining a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#Defining Dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

#Assessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

#Creating a mixed-type list
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))
    

#creating a car inventory program.
import csv
import copy
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
myInventoryList = []

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
currentVehicle = copy.deepcopy(myVehicle)

for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
        print("-----")
        
#working with the if statement.
userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
#working with else statement    
else:
    print("Please come back when you need to ship a package. Thank you.")
    
#Another example
CustomerReply = input("Do you want a home service? (Enter yes or no) ")
if CustomerReply == "yes":
    print("We can offer you home service!")
else:
    print("You can come around to our office, the opening hours is 8am - 5pm")
    
#working with elif statement. it is used when there is multiple con
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")
    
#working with a while loop.
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#importing random and writing a while loop.
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))




      
    