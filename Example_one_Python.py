# # Online exam qualification
# registered = input("Are you registered: yes/no")
# tuition_fee = input("Are the tuition fee paid:")

# if tuition_fee == "yes" and registered == "yes":
#     print("Cleared for the exam")
# elif tuition_fee == "no" and registered == "yes":
#      print("Not allowed for exam")
# else:
#     print("You are nor allowed to come to school")

    
#  # Cheking a number
# number = int(input("Enter a number:"))

# if number > 0:
#     print("The number is positive")
# elif number < 0:
#      print("The number is negtive")
# else:
#     print("The number is neutral")  


# # Grading system simulation
# Grade = float(input("Enter your grades: "))
# if Grade > 80:
#     print("You are in grade A")
# elif Grade >= 70:
#     print("You are in grade B")
# elif Grade >= 60:
#     print("You are in grade C")
# elif Grade >= 50:
#     print("You are in grade D")
# else:
#     print("You failed") 

# # Salary increment based on experince
# Salary = int(input("Your actual salary:"))
# Experience = int(input("Enter your years of experience:"))

# if Experience >= 10:
#     New_salary = Salary * 1.5
#     print(f"Your new salary is: {New_salary} Rwf")
    
# elif Experience >= 5:
#     New_salary = Salary * 1.2
#     print(f"Your new salary is: {New_salary} Rwf")
    
# else:
#     print(f"Your salary {Salary} Rwf")


# # display days of the week
# day = input("Enter the day of a week:")
# match day:
#     case "Monday":
#         print("This the first day of the week")
#     case "Tuesday":
#         print("This the second day of the week")
#     case "Wednsay":
#         print("This the third day of the week")
#     case "Thursday":
#         print("This the fourth day of the week")
#     case "Friday":
#         print("This the fify day of the week")
#     case "Satarday":
#         print("This the sixth day of the week")
#     case "Sunday":
#         print("This the seventh day of the week")
#     case _:
#         print("The is no corresponding day to your input")


# # Traffic light simulation
# Traffic_light = input("Enter the color representing a traffic light")
# match Traffic_light:
#     case "Red" | "red":
#         print("Please Stop the Vehicle!")
#     case "Yellow" | "yellow":
#         print("Please Go Slow!")
#     case "Green" | "green":
#         print("Please Start Moving!")
#     case _ :
#         print("You Entered The Invalid Input")

# # Example of loan Request simulation
# credit_score = int(input("Enter the Credit Score:"))
# match credit_score:
#     case score if score >= 750:
#         print("Loan Approved!")
#     case score if 650 <= score < 750:
#         print("Loan Approved with a Condition For Now")
#     case score if 550 <= score < 650:
#         print("Loan requires manual Review")
#     case _ :
#         print("Your Loan is Rejected Please!")
    
# Function
def greeting():
    print("Hello world!!")
    
greeting()       