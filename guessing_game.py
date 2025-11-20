import random

while True:
    try:
        n = int(input("Level: "))
        number = random.randint(1, n)
        break
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess == number:
            print("Just right!")
            break
        elif guess > number:
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        continue
