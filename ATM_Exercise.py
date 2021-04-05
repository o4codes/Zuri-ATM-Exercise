from datetime import datetime
from util.user_db import *
from util.atm_util import *
current_date = str(datetime.now().date()) #get date and cast to string
current_time = str(datetime.now().time()) # get time and cast to string
#show date on log in

name = input("Enter your name \n") #get name input from user
password = input("\nEnter your password \n") #get password input from user

response = login(name, password)

if response == "success":  
    print("\n Welcome "+name)
    print("Date: "+current_date+"\nTime: "+current_time)
    print("\n These are the available options")
    print("1, Check Balance")
    print("2, Withdrawal")
    print("3, Cash Deposit")
    print("4, Complaint")
    print("5, Password Change")
    print("6, Logout")

    selected_option = int(input("\n Please select an option: \n")) # get user selected option
    if selected_option == 1:
        balance = get_account(name)['balance']
        print("\nAccount Balance is "+str(balance)+"\n")
    elif selected_option == 2:
        amount_withdraw = float(input("\nHow much would you like to withdraw\n"))
        balance_left = 0
        try:
            balance_left = withdraw(get_account(name)['balance'],amount_withdraw)
        except AssertionError:
            print("amount to withdraw cannot be greater than current balance")
        else:
            update_account(name, password, balance_left)
            balance = get_account(name)['balance']
            print("\nBalance left: "+str(balance))
            print("Withdraw Succesful")

    elif selected_option == 3:
        deposit_amount = float(input("\nHow much would you like to deposit\n"))
        
    elif selected_option == 4:
        input("\nWhat issue would you like to report\n")
        print("\nThank you for contacting us")
    else:
        print("Invalid option selected, please try again")

elif response == "Invalid password": 
    print("Password Incorrect, please try again")   

else:
    print("Name not found, please try again")