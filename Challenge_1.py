import random

def get_secret_number():
    return random.randint(1,100)

secret = get_secret_number()
attempts = 0

def get_guess():
    return int(input("Guess the number(1-100):"))

def check_guess(secret,guess):
    if guess > secret:
        print("Too high")
        return False
    if guess < secret:
        print("Too low")
        return False
    else :
        print("Correct!")
        return True

while True:
    guess = get_guess()
    attempts += 1
    if check_guess(secret, guess) == True:
        break

print(f"You got in {attempts} attempts")



