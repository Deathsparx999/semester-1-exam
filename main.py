#### Describe each datatype below:(4 marks)
## 4         = integer(whole numbers)
## 5.7       = float(Numbers that can include decimals)
## True      = Boolean(True/false)
## Good Luck = String(words)

#### Which datatype would be useful for storing someone's height? (1 mark)
## Answer = float

#### Which datatype would be useful for storing someone's hair colour?(1 mark)
## Answer = string


####Create a variable tha will store the users name.(1 mark)
name=input("please enter your Name: ")
print("Hello",name,"thank you for answering")


####Create a print statement that will print the first 4 characters of the person's name.(3 marks)
str(name)
print(name[0:4])


####Convert the user's name to all uppercase characters and print the result
print(name.upper())

####Find out how many times the letter A occurs in the user's name
print("a appears in your name",name.count("a"),"times")



#### Create a conditional statement to ask a user to enter their age. If they are older than 18 they receive a message saying they can enter the competition, if they are under 18, they receive a message saying they cannot enter the competition.
age=int(input("please enter your age: "))
if age>=18:
  print("you are legable to enter the competition")
else:
  print("appologies but you are not old enough yet, please come back in",18-age,"years")

#### Create an empty list called squareNumbers (3 marks)
squareNumbers=[]

#### Square numbers are the solutions to a number being multiplied by itself( example 1 is a square number because 1 X 1 = 1, 4 is a square number because 2 X 2 = 4 ). 
###Calculate the first 20 square numbers and put them in the list called squareNumbers. (With loop and .append 10 marks, without, Max 6 marks).
for num in range (21):
  square=num*num
  squareNumbers.append(square)


####Print your list (1 mark)
print(squareNumbers)

####Create a variable called userSquare that asks the user for their favourite square number
userSquare=int(input("what is your favourite Square number user? "))

#### Add this variable to the end of your list called SquareNumbers
squareNumbers.append(userSquare)

### Create a variable called choice. This variable should choose a random element from your list. Print the variable called choice.(3 marks)
import random
choice=squareNumbers[random.randint(0,22)]
print(choice)

####Create another print statement that prints tha following output: The random square number is: XX, where XX is where the random square number chosen by the computer.(4 marks)
print("The random square number is",choice)