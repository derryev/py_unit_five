# Eva D
# 11/08/2023
# creates guessing game where user tries to guess a random number in each of three rounds,
# receiving a score at the end based on their average guesses per round.

counter = 0

import random
def get_guess():
    """
    Gets the user's guess for a number between 1 and 100, will not return/count guess unless it is from 1-100, if it is
    not loop will have user guess again.
    :return: the user's guess, a number from 1-100 (float)
    """
    while True:
        guess = float(input("Guess what number I am thinking of from 1-100: "))
        if guess<1 or guess>100:
            print(str(guess)+" isn't a number between 1 and 100.. try again")
        else:
            return guess


def get_number():
    """
    Generates and returns a random number from 1-100 that the user will try to guess.
    :return: the random number, which can be from 1-100 (float)
    """
    number = float(random.randint(1,100))
    return number


def give_feedback(number, guess):
    """
    Prints feedback to the user on their guesses of the number based on how far away from the number they are and on
    if they guessed too high or low.
    :param number: the computer generated number from 1-100 that the user is trying to guess (float)
    :param guess: the user's guess of the number (float)
    :return: nothing
    """
    if number > guess and number - guess <= 50:                                                                         # if the user is less than/equal to 50 away from the number, but guessed too low, the program will tell them this:
        print("You're less than 50 away! Just a little bit higher")
    elif number > guess and number - guess > 50:                                                                        # if user is more than 50 away from number and guessed too low, the program will tell them this:
        print("You're not close at all.. Try going higher...")
    elif number < guess and guess - number <= 50:                                                                       # if user is less than/equal to 50 away from number and guessed too high, the program will tell them this:
        print("You're less than 50 away! Just a little bit lower")
    elif number < guess and guess - number > 50:                                                                        # if user is more than 50 away from number and guessed too high, the program will tell them this:
        print("You're a liiiiitle (very) far away.. Try going lower...")


def tell_average(average_score, total_count):
    """
    Tells the user their score, which is based on the average guesses across all rounds, giving specific commentary
    based on how high the score is. Also tells user their total guesses because I thought that would be fun to know.
    :param average_score: the score the user earned (their total guesses across all rounds divided by three) (float)
    :param total_count: the total guesses a user made across all rounds. (int)
    :return: information on score/total guesses and commentary on how user did which is based on this score. (str)
    """
    if average_score < 5:                                                                                               # if the average score was less than 5 points, the user gets an extremely positive and congratulatory message
        return ("Wow! That was a great game. Your total score is "+str(average_score)+", which means that you averaged "    # when being told their average score and total guesses
                +str(average_score)+" guesses per game! You made a total of "+str(total_count)+" guesses.")
    elif 5< average_score<= 20:
        return ("You did pretty well. Your total score is " + str(average_score) + ", which means that you averaged "   # if the average score was from 6-20 points, the user gets a less enthusiastic but still positive message
              + str(average_score) + " guesses per game! You made a total of " + str(total_count) + " guesses.")            #when being told their average score and total guesses
    else:
        return("That game was PRETTY rough. Your total score is " + str(average_score) + ", because you averaged "      # if the average score was higher than 20 points, the user gets a playful message about how terribly they did
              + str(average_score) + " guesses per game. You made a total of " + str(total_count) + " guesses..."           # when being told their average score and total guesses
               "Don't worry..  I bet you'll do better next time!")


def main():
    print("Welcome to the guessing game! There are three rounds, in each of which you will try to guess a number I "
          "came up with from 1 to 100 in as few tries as possible.")
    total_count = 0
    round_count =0
    for x in range(3):
        round_count += 1                                                                                                # keeps track of which round it is
        counter = 1
        number = get_number()
        print("Round "+str(round_count)+"!")                                                                            # tells user which round it is at start of each round to help distinguish between all of the text in the program
        guess = get_guess()
        while number != guess:                                                                                          # while loop to keep repeating guessing while user is incorrect, adding to the round counter each time the user guesses
            give_feedback(number, guess)
            counter = counter +1
            guess = get_guess()
        if counter == 1:                                                                                                # if/else statement to have accurate grammar if player needed one or multiple tries (try/tries)
            print("Congratulations! It was "+str(number)+". You got the correct number in 1 try.")
        else:
            print("Congratulations! It was " + str(number) + ". You got the number in " + str(counter) + " tries.")
        total_count += counter                                                                                          # this adds to the total counter before the loop restarts so that the main counter can reset without the program loosing how many tries each round took, compiling the total tries for the end of the game.
    average_score=total_count/3                                                                                         # averages score by dividing the total tries by three (for three rounds)
    print(tell_average(round(average_score, 2), total_count))                                                           # prints command that will tell user their score, rounds avg score to two decimal points for telling the user so that the numbers given are not extremely long


main()
