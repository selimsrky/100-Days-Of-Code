# height = int(input("Please enter your height: "))
# if height >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("You cannot ride the rollercoaster")


# number = int(input("Please enter a number: "))

# if (number % 2 == 0):
#     print("Your number is even.")
# else:
#     print("your number is odd.")


#TICKET PRICE

# height = int(input("What's your height: "))
# age = int(input("How old are you?"))
# bill = 0
# if height > 120:
#     print("You can ride the rollarcoaster and")

#     if age < 12:
#         bill = 5
#         print("Child tickets are 5 dollars.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are 7 dollars.")
#     elif age > 18 and age < 45:
#         bill = 12
#         print("Adult tickets are 12 dollars.")
#     elif age >= 45 and age <= 55:
#         print("The rollercoaster is free for you.")

#     extra_price = input("Do you want the photos?(yes/no)")

#     if extra_price == "yes":
#        bill += 3 
#        print(f"You need to pay {bill} dollars.")
# else:
#     print("You cannot ride the rollercoaster")


# PIZZA ORDER PRACTICE
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S,M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N:")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1
    
# print(f"The total bill is: {bill} dollars.")




# PROJECT : TREASURE ISLAND

print("Welcome to Treasure Island. Your mission is to find the treasure.")
direction = input("Choose the direction you want to go.(left/right)").lower()
if direction == "left":
    path = input("You've come to a lake. There is an island in the middle of the lake. Do you want to swim or wait?").lower()
    if path == "wait":
        colour = input("You arrive the at the island unharmed. There is a house with 3 doors(red,yellow,blue). Which colour do you choose?")
        if colour == "yellow":
            print("You win the game!")
        else:
            print("Game over.") 
    else:
        print("Game over.")
else:
    print("Game over.")

