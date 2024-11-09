import random
import string 

length = int(input("Enter the length of your password :"))
password = None
uppercase_lowercase = input("Do you want uppercase and lowercase ?(yes/no):")
numbers_or_not = input("Do you want numbers or not ?(yes/no):")
special_characters = input("Do you want special characters or not ?(yes/no):")

char_only = string.ascii_lowercase
upper = string.ascii_letters
numbers = string.ascii_lowercase + string.digits
special = string.punctuation
num_upper = string.ascii_letters + string.digits
num_upper_special = string.ascii_letters + string.digits + string.punctuation

if (uppercase_lowercase == "yes"):
    for l in length:
        random.choice(upper)
    print(f"Your password is:\n {password}")

elif(uppercase_lowercase == "yes" and numbers_or_not == "yes"):
    for l in length:
        random.choice(num_upper)
    print(f"Your password is :\n {password}")

elif(uppercase_lowercase ==  "yes" and numbers_or_not == "yes" and special_characters == "yes"):
    for l in length:
        password = random.choice(num_upper_special)
    print(f"Your password is :\n {password}")