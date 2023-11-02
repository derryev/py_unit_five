def fibonacci(number):
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
    sequence = ""
    a=1
    b=1
    for x in range(number-2):
        c = a+b
        sequence += str(c)+" "
        a=b
        b=c
    sequence = str("1 1 ")+sequence
    return sequence
def main():

    numbers_in_sequence = int(input("How many numbers of the fibonacci sequence do you want to see?"))
    print(fibonacci(numbers_in_sequence))

main()