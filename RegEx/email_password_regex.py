import re
import sys

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+$)")
password_pattern = re.compile(r"(^[a-zA-Z0-9$#@%]{10}$)")

email = str(input('Enter Email: '))

if (email_pattern.search(email)):
   print(f'{email} is a valid Email address')

else:
   print("Invalid Email address")


# Set the initial password as False 
password = False

# Password Strength Checker
def check_password_strength():

    passwordText = input('Enter Password: ')

    charRegex = re.compile(r'(\w{8,})')   # Check if password has at least 8 characters
    lowerRegex = re.compile(r'[a-z]+')    # Check if at least one lowercase letter
    upperRegex = re.compile(r'[A-Z]+')    # Check if at least one upper case letter
    digitRegex = re.compile(r'[0-9]+')    # Check if at least one digit.
    symbolRegex = re.compile(r'[@#$%]+')  # Check if at least one symbol.

    if charRegex.findall(passwordText) == []: 
        print('Password must contain at least 8 characters')

    elif lowerRegex.findall(passwordText)==[]: 
        print('Password must contain at least one lowercase character')

    elif upperRegex.findall(passwordText)==[]: 
        print('Password must contain at least one uppercase character')

    elif digitRegex.findall(passwordText)==[]: 
        print('Password must contain at least one digit character')

    elif symbolRegex.findall(passwordText)==[]: 
        print('Password must contain at least one symbol character')  

    # Provided the above 4 conditions are satisfied
    else:  
        print('Password is strong.')
        global passStrong 
        passStrong = True
        return 

check_password_strength()