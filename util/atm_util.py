""" 
Module holds ATM functions
Withdraw and Deposit functions for each User
"""

def withdraw(current_balance,withdraw_amount):
    assert withdraw_amount < current_balance, "amount to withdraw cannot be greater than current balance"        
    return current_balance - withdraw_amount

def deposit(current_balance, deposit_amount):
    return current_balance + deposit_amount

