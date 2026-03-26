# Example of loan Request simulation
credit_score = int(input("Enter the Credit Score:"))
match credit_score:
    case score if score >= 750:
        print("Loan Approved!")
    case score if 650 <= score < 750:
        print("Loan Approved with a Condition For Now")
    case score if 550 <= score < 650:
        print("Loan requires manual Review")
    case _ :
        print("Your Loan is Rejected Please!")