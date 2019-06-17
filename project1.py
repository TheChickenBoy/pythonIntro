import random

while(True): # loop until a number is given
    userIn = input("How many games would you like to play? ") 
    try:
        nr = int(userIn) # Convert into an integer
        break # Leave loop
    except:
        print("Not natural number")


for i in range(nr): # Main game loop
    rand = random.randint(1,26) # Number 1-25
    nrGuess = 0
    while(True):
        try:
            guess = int(input("Guess a number (1-25): "))
            nrGuess += 1
            if guess == rand:
                print("Correct number (%d) was guessed in %d turns" % (rand, nrGuess))
                break
            elif guess < rand:
                print("Guess to small")
                continue
            else:
                print("Guess to large")
                continue
        except:
            pass # Could add error handling for incorect input there aswell
