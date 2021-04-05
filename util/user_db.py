""" 
Module holds User CRUD Functions
Also holds Database of users (not persisted)
"""

accounts_database = [
    {'name':'Seyi', 'password':'passwordSeyi','balance':0},
    {'name':'Mike', 'password':'passwordMike','balance':0},
    {'name':'Love', 'password':'passwordLove','balance':0}
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
    

def create_account(name, password):
    if type(name) != str and type(password) != str:
        raise TypeError
    user_list = list(filter(lambda account: account['name'] == name, accounts_database))
    if user_list == []:
        new_user = {'name': name, 'password': password, 'balance':0 }
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

    