def get_input():
    """
    This function ensures that a user correctly enters a number in the proper range.
    :return: a value between 1 and 10, inclusive
    """
    while True:
        user_choice = input("Please choose a number between 1 and 10: ")
        if float(user_choice) < 1 or float(user_choice) > 10:
            print("Don't forget! You need to enter a number between 1 and 10, not "+str(user_choice))
        elif float(user_choice) >= 1 or float(user_choice) <= 10:
            break
    return user_choice

def main():
    print(get_input())


if __name__ == '__main__':
    main()
