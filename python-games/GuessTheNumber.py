import random

print("\nWelcome to Guess The Number idiot")
print("You only got 5 tries, let see how slow you are\n")

guessesTaken = 0
number = random.randint(1, 3)

while guessesTaken < 5:
    print("So...What's your guess? ")
    guess = int(input())
    guessesTaken = guessesTaken + 1

    if guess < number:
        print("That's wayyy too low you fucking moron\n")
    elif guess > number:
        print("That's too high loser\n")
    elif guess == number:
        break

if (guess == number) and guessesTaken < 4:
    guessesTaken = str(guessesTaken)
    print("Wowowow! You are a fucking cheater! only " + guessesTaken + " tries?!")
    print("Noice!")
elif guess == number:
    print("Noice!")
elif guess != number:
    guessesTaken = str(guessesTaken)
    print("Such a loser... It took you " + guessesTaken + " tries to show us the genius you are not.\n")
