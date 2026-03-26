# Traffic light simulation
Traffic_light = input("Enter the color representing a traffic light")
match Traffic_light:
    case "Red" | "red":
        print("Please Stop the Vehicle!")
    case "Yellow" | "yellow":
        print("Please Go Slow!")
    case "Green" | "green":
        print("Please Start Moving!")
    case _ :
        print("You Entered The Invalid Input")