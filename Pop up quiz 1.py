# # Question 1 If condition
# # Print whether a number is Positive, Negative or Zero
# Number = float(input("Enter a number of your choice: "))
# if Number > 0:
#     print("The number you entered is Positive")
# elif Number < 0:
#     print("The number you entered is Negative")
# else:
#     print("The number you entered is Zero")



# Question 2 If condition
# Print whether someone is A Child, Teenager, Adult
# Age = int(input("Enter your age: "))
# if Age > 19:
#     print("You ar an Adult")
# elif 13 <= Age <= 19:
#     print("You are a Teen")
# elif Age < 13:
#     print("You are a Child")
# else:
#     print("Invalid input")

# # Question 3 Match-case
# # Print the day of the week corresponding to the entered number
# Day = int(input("Enter a day of the week: "))
# match Day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid Input")

# Question 4 Fuction
# A function that returns a square of a number entered
num = float(input("Enter a number: "))
def Square(num):
    return num * num
    
num_squared = Square(num)
print("The number you entered squared is: ", num_squared)

# #Question 5 Fuction + If condition
# # A function that checks whether a number is Even or Odd
# number = float(input("Enter a number: "))
# def Check_number(number):
#     if number % 2 == 0:
#         print("The number is Even")
#     elif number % 2 == 1:
#         print("The number is Odd")
#     else:
#         print("Invalid input")


# Check_number(number)
    
