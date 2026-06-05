import re

#Sanket2020
username=input("Enter your username:")

x=re.findall('[A-Z]+[a-z]+[0-9]',username)

if x:
    print("Username is valid!")
else:
    print("Error!Username is not valid...")

