Order = int(input("Enter the number corresponding to your order: "))
match Order:
    case 1 :
        print("You have ordered Food:")
    case 2 :
        print("You have ordered Apple juice:")
    case 3 :
        print("You have ordered Ice cream:")
    case 4 :
        print("You have ordered only Soft drink:")
    case 5 :
        print("You have ordered only Food:")
    case _ :
        print("We don't have your order")