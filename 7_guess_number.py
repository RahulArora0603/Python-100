import random

def guess():
    num = int(input("Enter a number between 0 and 100 to guess."))
    if num>100 | num<1:
        raise ValueError(print("Enter number between 1 to 100."))
    else:
        r_num = random.randint(1,100)
        if num==r_num:
            print("You guessed it right")
        else:
            print("Try again")            

guess()