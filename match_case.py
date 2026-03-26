# display days of the week
day = input("Enter the day of a week:")
match day:
    case "Monday":
        print("This the first day of the week")
    case "Tuesday":
        print("This the second day of the week")
    case "Wednsay":
        print("This the third day of the week")
    case "Thursday":
        print("This the fourth day of the week")
    case "Friday":
        print("This the fify day of the week")
    case "Satarday":
        print("This the sixth day of the week")
    case "Sunday":
        print("This the seventh day of the week")
    case _:
        print("The is no corresponding day to your input")
         