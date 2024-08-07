# GUESS THE NUMBER
import random

user = 0
tries = 0
answer = random.randint(1, 100)

while user != answer:
    user = int(input("Enter a number between 1 and 100: "))
    tries += 1
    if user < answer:
        print("Your guess was too low.")
    elif user > answer:
        print("Your guess was too high.")
    else:
        print("You got it!")
        print("You have tried", tries, "times.")

# Bus Fare
start = int(input("What number stop are you at? "))
end = int(input("What is the stop you want to go to? "))
BUS_FARE = 5
FARE_PER_STOP = 2.5
fare = BUS_FARE + (end - start) * FARE_PER_STOP

print(f"The fare from Stop 3 to Stop 4 is ${fare}")

# Is it a Strong Password?
pwd = input()
score = 0

if len(pwd) > 7:
    print("len > 7")
    score += 1

for char in pwd:
    if char.isupper():
        print("has upper")
        score += 1
        break

for char in pwd:
    if char.islower():
        print("has lower")
        score += 1
        break

for char in pwd:
    if char.isdigit():
        print("has digit")
        score += 1
        break

if not pwd.isalnum():
    print("has special")
    score += 1

print("Password score", score)

# Guess the Number (Through Letters)
import random

ALPHABETIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
user = 0
tries = 0
answer = random.randint(1, 26)

print(ALPHABETIC[answer-1])
while user != answer:
    user = input("Enter a letter: ").upper()
    tries += 1
    user = ALPHABETIC.index(user) + 1
    if user < answer:
        print("Your guess was too low.")
    elif user > answer:
        print("Your guess was too high.")
    else:
        print("You got it!")
        print("You have tried", tries, "times.")