name = input("Please enter your name: ")
print("Hello", name, "! Welcome to the adventure! ")

while True:
    answer = input("You are on a bike and you reach a dead end. You can go either LEFT or RIGHT. Please choose! ").lower()

    if answer == 'left':
        answer1 = input("On taking left, you find a bridge and a river with crocodiles. Please choose either BRIDGE or RIVER ").lower()

        if answer1 == 'bridge':
            print("You reach the house safely!")
            break
        elif answer1 == 'river':
            print("Wrong move! You die")
            continue
        else:
            print("Incorrect answer! You Lose.")
            continue

    elif answer == 'right':
        answer2 = input("On taking right, you find a car and a cycle. Please choose either CAR or CYCLE ").lower()

        if answer2 == 'car':
            print("You reach the house safely!")
            break
        elif answer2 == 'cycle':
            print("Wrong move! You die")
            continue
        else:
            print("Incorrect answer! You Lose.")
            continue
    else:
        print("Incorrect answer! You Lose.")


print("Thanks for playing ", name)