from datetime import datetime
""" 
Module holds User CRUD Functions
Also holds Database of users (not persisted)
"""

accounts_database = [
    {'name':'Seyi', 'account_number':'2012345670', 'password':'passwordSeyi','balance':0},
    {'name':'Mike','account_number':'2012673487', 'password':'passwordMike','balance':0},
    {'name':'Love','account_number':'2201234567', 'password':'passwordLove','balance':0}
]


def login(name,password):
    if type(name) != str and type(password) != str:
        raise TypeError 
    user_list = list(filter(lambda account: account['name'] == name, accounts_database))
    
    if user_list == []:
        return "user not found"
    else:
        if user_list[0]['password'] == password:
            return "success"
        else:
            return "Invalid password"

def generate_account_number():
    gen_number = datetime.now().timestamp()
    account_number = str(gen_number).split(".")[0]
    return account_number
      
def create_account(name, password):
    if type(name) != str and type(password) != str:
        raise TypeError
    user_list = list(filter(lambda account: account['name'] == name, accounts_database))
    if user_list == []:
        account_number = generate_account_number()
        new_user = {'name': name,'account_number':account_number, 'password': password, 'balance':0 }
        accounts_database.append(new_user)
        return True
    else:
        return False

def update_account(name, password, balance):
    if type(name) != str: raise TypeError
    for account in accounts_database:
        if account['name'] == name:
            account['password'] = password
            account['balance'] = balance
            break

def get_account(name):
    if type(name) != str:
        raise TypeError
    user_list = list(filter(lambda account: account['name'] == name, accounts_database))
    return user_list[0]

