# fruits = ["Apple","Peach","Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie ")
#     print(fruits)
# print("Hello World")

# student_scores = [150,142,185,329,120,171,184,149,199,24]

# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)

# sum = 0
# for number in range(1,101):
#     sum += number
# print(sum)

# list = [1,2,3,4,5,6,7,8,9,10]

# total = 0
# for number in list:
#     total += number
# print(total)


# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# PASSWORD GENERATOR

import random

password = []

print("Welcome to the Password Generator")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",  
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbols = ["!", "#", "$", "%", "^", "&", "*", "(", ")", "?"]

numbers = ["0","1","2","3","4","5","6","7","8","9"]

amount_of_letter = int(input("How many letters would you like in your pass word?\n"))

amount_of_symbol = int(input("How many symbols would yoU like?\n"))

amount_of_number = int(input("How many numbers would you like?\n"))

for letter in range(0,amount_of_letter):
    password += random.choice(letters)

for symbol in range(0,amount_of_symbol):
    password += random.choice(symbols)

for number in range(0,amount_of_number):
    password += random.choice(numbers)

print(password)
newpassword = []
for elements in password:
    newpassword += random.choice(password)

newpassword = "".join(newpassword)

print(f"Your new password is: {newpassword}")





