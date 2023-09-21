import random

char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!$&1234567890'

numOfPasswords = int(input("How many passwords would you like to generate? "))

length = int(input("What would you like the length for the password? "))


for f in range(numOfPasswords):
    password = ''
    for i in range(length):
        password += random.choice(char)
    print("Password: " + password)