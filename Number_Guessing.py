import random

top_range = input("Type a number for your top range: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please enter number greater than 0, next time! ")
        quit()
else:
    print('Please enter a number next time.')
    quit()

random_number= random.randint(0,top_range)

guess_count = 0
while True:
    guess_count += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print('Please enter a number next time.')
        continue

    if user_guess == random_number:
        print("Wohooo! Its a match!")
        break
    elif user_guess < random_number:
        print("Your guess is below the desired number. Try Again! ")
    else:
        print("Your guess is above the desired number. Try Again! ")

print("You guessed it correct after " + str(guess_count) + " guesses.")
