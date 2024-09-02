import os

def clear_screen():
    os.system("cls")
    
print("*********Welcome to Silent Auction***********")

def highest_bidder():
    bidding_data = {}
    while True:
        name = input("Enter your name: ")
        is_company = input("Are you from a company? (yes/no): ").lower()
        if is_company == "yes":
            company_name = input("Enter the name of your company: ")
        else:
            company_name = None
        
        bid = int(input("Enter your bid value: "))
        bidding_data[name] = {"Company": company_name, "Bid": bid}
        check = input("Is there any other bidder? ").lower()
        clear_screen()  # Clear the screen
        if check != "yes":
            break
    
    highest_bidder_name = ""
    highest_bid = 0
    for name, data in bidding_data.items():
        if data["Bid"] > highest_bid:
            highest_bid = data["Bid"]
            highest_bidder_name = name
            company_name = data["Company"]
    if company_name:
        print(f"The highest bidder is {highest_bidder_name} from company {company_name} with a bid of Rs. {highest_bid}")
    else:
        print(f"The highest bidder is {highest_bidder_name}, local, with a bid of Rs. {highest_bid}")
        
highest_bidder()
