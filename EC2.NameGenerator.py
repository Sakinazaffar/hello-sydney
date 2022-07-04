# ec2 names generator

name = input("Please enter your name:   ")
department = input("which department are you from?   ")

print("Hello " + name)
print("from " + department)


while True:
    try:
        number_ec2 = int(input("how many ec2 instances do you require ?  please enter only digits:  "))
    except ValueError:
        print("Sorry, I don't understand that")
        continue
    else:
        break

def gen(ec2_range):
    for i in range(ec2_range):
        yield i

from random import randint

def ec2_character(nbr_of_chars):
    return "".join(chr(randint(33,126)) for i in range(nbr_of_chars))


import random
letters = ("s", "a", "k", "i", "n", "a" )
digits = ("0", "1", "2", "3", "4", "5")

unique_name = "".join(random.choice(letters)  + "" + random.choice(digits) for _ in range(5))

for i in gen(number_ec2):
    i = id(i)
    n = (department + str(i))

    print(n + unique_name + ec2_character(5))

