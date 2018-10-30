# -*- coding: utf-8 -*- 

import random

secret = random.randint(1,100)
guess = 0
tries = 0

print(r'Im the Dread Pirate Roberts, and  I have a secret')
print("It is a number from 1 to 99, I'll give you 6 tries")

while guess != secret and tries < 6:
    guess = input("what are you guess:")
    guess = int(guess)
    if guess < secret:
        print('too low, ye scurvy dog!')
    elif guess > secret:
        print('too high, landlubber!')
    tries = tries + 1
if guess == secret:
    print('avast')
else:
    print('no more guess! ')
    print('the secret number was {0}'.format(secret))