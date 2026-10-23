#benjamin maddux p1 ms larose
import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number: #forgot a : what made the indentation not work
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print(f"Your guesses per round: {scores}")#i did a f-string and it worked

total = 0
for score in scores:
    # didnt need that total 0 it was useless and it was a syntacx error
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(average.round[2]))#rounded

best_round = scores[0]
for i in range(1, rounds):#get rid -1 becuse the code didnt work when there
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")