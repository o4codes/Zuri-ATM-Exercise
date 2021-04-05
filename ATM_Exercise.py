from datetime import datetime

current_date = str(datetime.now().date()) #get date and cast to string
current_time = str(datetime.now().time()) # get time and cast to string

allowed_users = ['Seyi','Mike','Love']
allowed_password = ['passwordSeyi','passwordMike','passwordLove']

name = input("Enter your name \n") #get name input from user

if name in allowed_users:
    password = input("\nEnter your password \n") #get password input from user
    user_id = allowed_users.index(name)  #get user id from position of name in list

    if(password == allowed_password[user_id]):
        print("\n Welcome "+name)
        print("Date: "+current_date+"\nTime: "+current_time)
        print("\n These are the available options")
        print("1, Withdrawal")
        print("2, Cash Deposit")
        print("3, Complaint")

        selected_option = int(input("\n Please select an option: \n")) # get user selected option
        if (selected_option == 1):
            input("\nHow much would you like to withdraw\n")
            print("\nTake your cash")
        elif(selected_option == 2):
            deposit_amount = float(input("\nHow much would you like to deposit\n"))
            print("\nCurrent balance: "+str(deposit_amount))
        elif(selected_option == 3):
            input("\nWhat issue would you like to report\n")
            print("\nThank you for contacting us")
        else:
            print("Invalid option selected, please try again")

    else: 
        print("Password Incorrect, please try again")   

else:
    print("Name not found, please try again")