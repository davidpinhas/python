import random

print("\nWelcome to Guess The Number idiot")
print("You only got 5 tries, let see how slow you are\n")

guessesTaken = 0
number = random.randint(1, 20)

while guessesTaken < 5:
    print("So...What's your guess? ")
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:
        print("That's wayyy too low you fucking moron\n")
    if guess > number:
        print("That's too high loser\n")
    if guess == number:
        break

if (guess == number) and guessesTaken < 4:
    guessesTaken = str(guessesTaken)
    print("Wowowow! You are a fucking cheater! only " + guessesTaken + " try?!")
if guess == number:
    print("Noice!")
if guess != number:
    guessesTaken = str(guessesTaken)
    print("Such a loser... It took you " + guessesTaken + " to show us the genius you are not.\n")
