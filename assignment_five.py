


def get_guess():
    while True:
        guess = float(input("Guess what number I am thinking of from 1-100: "))
        if guess<1 or guess>100:
            print(str(guess)+" isn't a number between 1 and 100.. try again")
        else:
            break



import random

def get_number():
    number = random.randint(1,100)
    return number

def main():
    for x in range(3):
        number = get_number()
        print(number)
        get_guess()



main()
counter = 0





counter += counter