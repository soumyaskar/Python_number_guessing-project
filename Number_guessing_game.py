import random
import math

# Input bounds
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# Generating the random number between the lower and upper bound
x = random.randint(lower, upper)

# Calculate maximum chances
max_attempts = math.ceil(math.log(upper - lower + 1, 2))
print(f"\n\tYou've only {max_attempts} chances to guess the integer\n")

# Initialize number of guesses
count = 0

# Loop for guessing
while count < max_attempts:
    count += 1
    guess = int(input("Guess the number: "))

    # Condition testing
    if x == guess:
        print(f"Congratulations! You did it in {count} try/tries.")
        break
    elif x > guess:
        print("Your guess is too small!")
    else:
        print("Your guess is too high!")

# If all attempts are used
if count >= max_attempts and x != guess:
    print(f"The number is {x}")
    print("\tBetter luck next time!!")
