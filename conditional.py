import random


print("------------------------")
print("    M&M Guessing Game   ")
print("------------------------")

print("Guess the number of M&Ms in the jar")
print()
mm_count = random.randint(1,100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    guess_text = input("So, How many M&Ms are in the Jar? ")
    guess = int(guess_text)
    print(guess)

    if mm_count == guess:
        print("You W-I-N!")
        break
    elif guess < mm_count:
        print("Sorry, too LOW")
    else:
        print("Nope, too HIGH")

    attempts += 1

print(f"It was {mm_count}. BYe")
