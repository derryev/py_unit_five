
counter=0
total=0
print("In this program, you can enter as many numbers as you'd like to find their average")
while True:
    user_choice = input("Enter a number or q to quit: ")
    if user_choice=="q":
        if counter==0:
            print("Goodbye :(")
            break
        print("You entered "+str(counter)+" numbers")
        print("Your total is "+str(total))
        print("The average of your entered numbers is "+str((total/counter)))
        break
    counter += 1
    total += int(user_choice)