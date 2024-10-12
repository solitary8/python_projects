import random
import string
import time

print("-------Welcome to The Password Generator !---------------")
time.sleep(1)

data_numbers_chars = string.ascii_lowercase + string.ascii_uppercase + "0123456789" + "&!#(-|_ç),;."
data_alphabet = string.ascii_lowercase + string.ascii_uppercase

length = int(input("Input the length in number of characters that you want your password to be : "))

numbers_characters = input("Do you want numbers and characters ?(y/n):")
password = ""

for pwd in range(length):
    if(numbers_characters == "y"):
        password += random.choice(data_numbers_chars)
    
    elif(numbers_characters == "n"):
        password += random.choice(data_alphabet)

print("Your password is  : ",password)