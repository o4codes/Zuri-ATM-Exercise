from datetime import datetime
from util.user_db import *
from util.atm_util import *

#contains user console page for first section
def home_page():
    while True:
        print("\nHello, Welcome !!!!")
        
        print("1, Register")
        print("2, Login")
        print("3, Exit")

        try:
            response = int(input("\nPlease enter the digit to select an option\n"))
        except ValueError:
            print("Ensure a digit is specified")
        else:              
            if response == 1:
                register_page()
                break
            elif response == 2:
                user_page()
                break
            elif response == 3:
                print("Thank you for banking with us")
                break
            else:
                print("\nInvalid Option selected")

#contains user console page for register section
def register_page():
    while True:
        print("\nPlease fill the following details to create an account")
        name = input("\nEnter your name\n")
        password = input("\nEnter your password\n")
        response = create_account(name,password)
        if response:
            print("\nAccount created successfully")
            print("\nYou will be redirected to the home page")
            home_page()
            break
            
        else:
            print("\nAccount creation Failed")
            print("User with name already exist")
            try:
                reply = int(input("\nEnter 0 to redirect to HomePage \nEnter 1 to retry account creation\n"))
            except ValueError:
                print("Invalid response, you will be redirected home")
                home_page()
                break 
            else: 
                if reply == 0:
                    home_page()
                    break               

#contans user console page for user profeil actions           
def user_page(): 
    current_date = str(datetime.now().date()) #get date and cast to string
    current_time = str(datetime.now().time()) # get time and cast to string
    #show date on log in

    print("\nLogin")
    name = input("Enter your name \n") #get name input from user
    password = input("\nEnter your password \n") #get password input from user

    response = login(name, password)

    while True:
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

            try:
                selected_option = int(input("\nPlease enter digit to select an option: \n"))
            except ValueError:
                print("Invalid response, response must be a digit")
            else:
                if selected_option == 1:
                    balance = get_account(name)['balance']
                    print("\nAccount Balance is "+str(balance)+"\n")

                elif selected_option == 2:             
                    balance_left = 0
                    try:
                        amount_withdraw = float(input("\nHow much would you like to withdraw\n"))
                        balance_left = withdraw(get_account(name)['balance'],amount_withdraw)
                    except AssertionError:
                        print("amount to withdraw cannot be greater than current balance")
                    except ValueError:
                        print("Amount must be a number")
                    else:
                        update_account(name, password, balance_left)
                        balance = get_account(name)['balance']
                        print("\nBalance left: "+str(balance))
                        print("Withdraw Succesful")

                elif selected_option == 3:
                    try:
                        deposit_amount = float(input("\nHow much would you like to deposit\n"))
                    except ValueError:
                        print("Amount must be a number")
                    else:
                        current_balance = deposit(get_account(name)['balance'],deposit_amount)
                        update_account(name,password,current_balance)
                        balance = get_account(name)['balance']
                        print("\nBalance left: "+str(balance))
                        print("Deposit Succesful")

                elif selected_option == 4:
                    input("\nWhat issue would you like to report\n")
                    print("\nThank you for contacting us")

                elif selected_option == 5:
                    confirm_password = input("\nPlease your enter your former password\n")
                    if confirm_password == get_account(name)['password']:
                        new_password = input("\nPlease your enter your new password\n")
                        balance = get_account(name)['balance']
                        update_account(name,new_password,balance)
                        print("\nAccount password updated successfully")
                    else:
                        print("\nWrong password")

                elif selected_option == 6:
                    print("You will be redirected to the home page")
                    home_page()
                    break

                else:
                    print("Invalid option selected, please try again")
                
        elif response == "Invalid password": 
            print("Password Incorrect") 
            try:
                reply = int(input("\nEnter 0 to redirect to HomePage \nEnter 1 to retry account creation\n"))
            except ValueError:
                print("Invalid response, you will be redirected home")
                home_page()
                break  
            else:
                if reply == 0:                   
                    home_page()
                    break   

        else:
            print("Name not found, please try again")
            try:
                reply = int(input("\nEnter 0 to redirect to HomePage \nEnter 1 to retry account creation\n"))
            except ValueError:
                print("Invalid response, you will be redirected home")
                home_page()
                break
            else:
                if reply == 0:                   
                    home_page()
                    break   

#launch home console   
home_page()