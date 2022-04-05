print("Hello! Good Morning! ")
name = input("Please enter your name: ").upper()

print("Welcome! " + name)
playing = input("\nDo you want to play the Quiz ? ").lower()

if playing != 'yes':
    print("As your response was not yes, Quitting!")
    quit()
else:
    print('OK ' + name + ' Lets Play! ')
    score = 0

    answer = input("Question: What does CPU stands for? ").upper()
    if answer == 'CENTRAL PROCESSING UNIT':
        print("Correct Answer! ")
        score += 1
    else:
        print("Incorrect Answer! ")

    answer = input("Question: What does PSU stands for? ").upper()
    if answer == 'POWER SUPPLY UNIT':
        print("Correct Answer! ")
        score += 1
    else:
        print("Incorrect Answer! ")

    answer = input("Question: What does GPU stands for? ").upper()
    if answer == 'GRAPHICS PROCESSING UNIT':
        print("Correct Answer! ")
        score += 1
    else:
        print("Incorrect Answer! ")

    answer = input("Question: What does RAM stands for? ").upper()
    if answer == 'RANDOM ACCESS MEMORY':
        print("Correct Answer! ")
        score += 1
    else:
        print("Incorrect Answer! ")

    print("Quiz Complete. You got " + str(score) + " out of 4 questions correct ")