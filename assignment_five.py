# Eva D
# November 8, 2023
# explanation

counter = 0

import random
def get_guess():
    while True:
        guess = float(input("Guess what number I am thinking of from 1-100: "))
        if guess<1 or guess>100:
            print(str(guess)+" isn't a number between 1 and 100.. try again")
        else:
            return guess


def get_number():
    number = random.randint(1,100)
    return number


def give_feedback(number, guess):
    if number > guess and number - guess <= 50:
        print("You're less than 50 away! Just a little bit higher")
    elif number > guess and number - guess > 50:
        print("You're not close at all.. Try going higher...")
    elif number < guess and guess - number <= 50:
        print("You're less than 50 away! Just a little bit lower")
    elif number < guess and guess - number > 50:
        print("You're a liiiiitle (very) far away.. Try going lower...")


def tell_average(average_score, total_count):
    if average_score < 5:
        return ("Wow! That was a great game. Your total score is "+str(average_score)+", which means that you averaged "
                +str(average_score)+" guesses per game! You made a total of "+str(total_count)+" guesses.")
    elif 5< average_score<= 20:
        return ("You did pretty well. Your total score is" + str(average_score) + ", which means that you averaged "
              + str(average_score) + " guesses per game! You made a total of " + str(total_count) + " guesses.")
    else:
        return("That game was PRETTY rough. Your total score is " + str(average_score) + ", because you averaged "
              + str(average_score) + " guesses per game. You made a total of " + str(total_count) + "guesses... wow")


def main():
    total_count = 0
    for x in range(3):
        counter = 1
        number = get_number()
        #print(number)
        guess = get_guess()
        while number != guess:
            give_feedback(number, guess)
            counter = counter +1
            guess = get_guess()
        if counter == 1:
            print("Congratulations! It was "+str(number)+". You got the correct number in 1 try.")
        else:
            print("Congratulations! It was " + str(number) + ". You got the number in " + str(counter) + " tries.")
        total_count += counter
    average_score=total_count/3
    print(tell_average(round(average_score, 2), total_count))


main()
