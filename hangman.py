import random
import os
import sys

words = [
    "red",
    "yellow",
    "pink",
    "green",
    "purple",
    "blue"
]

def clear():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses,good_guesses,target):
    clear()

    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter,end='')
    print('\n\n')

    for letter in target:
        if letter in good_guesses:
            print (letter,end='')
        else:
            print ('_',end='')
    print('')
    print('')

def get_guess(bad_guesses,good_guesses):
    while True:
        guess = input("What's your guess? ").lower()
        if len(guess) != 1:
            print("you can only guess one letter at a time")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("you've already guessed that letter")
            continue
        elif not guess.isalpha():
            print("You can only guess letters")
            continue
        else:
            return guess

def play(done):
    clear()
    target = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses,good_guesses,target)
        guess = get_guess(bad_guesses,good_guesses)

        if guess in target:
            good_guesses.append(guess)
            found=True
            for letter in target:
                if letter not in good_guesses:
                    found = False
            if found == True:
                print("You win")
                print("The secret word was {}".format(target))
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses,target)
                print("you lost")
                print("the secret word was {}".format(target))
                done=True

        if done:
            play_again = input("Do you want to play again? y/n ")
            if play_again.lower() != 'n':
                return play(done=False)
            else:
                sys.exit()

print("Welcome to Hangman")
done=False
while True:
    clear()
    play(done)

# draw guessed letter and strikes
# print out win/lose
