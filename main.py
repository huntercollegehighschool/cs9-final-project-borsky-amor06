"""
Name(s): Brian Gorsky 
Name of Project: Mr Cheng's Personal Hangman Game 
"""

import time
import random
from words import word_list


print("Welcome to this game of Hangman, brought to you by HangBot (but you can call me Brian for short). What is your name?")
time.sleep(3)
name = input ("Enter your name, challenger: ")
print("Hello " + name + " , I hereby challenge you to a game of Hangman. Let's see what you got. Good luck, you're going to need it!")
time.sleep(4)
print("Your game is about to start")
time.sleep(3)

def get_word():
  word = random.choice(word_list) 
  return word.upper()

def play(word):
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  print(display_hangman(tries))
  print(word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Please guess either a letter or a word: ").upper()
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
       print("That's a good guess, but unfortunately you already guessed the letter", guess) 
      elif guess not in word:
        print("I'm sorry but", guess, "is not found in this word")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print("Oh wow, you got it!", guess, "is in the word!")
        guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(word)if letter == guess]
        for index in indices:
          word_as_list[index] = guess
        word_completion = "".join(word_as_list)
        if "_" not in word_completion:
          guessed = True
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("Hey! You already guessed that word:", guess)
      elif guess != word:
        print(guess, "is not the word.")
        tries -= 1
        guessed_words.append(guess)
      else:
        guessed = True
        word_completion = word

    else: 
      print("Nice try, but that guess won't work here.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
  if guessed:
    print("Congrats, I didn't think you had it in you. You guessed the word!!!")
  else:
    print("That's quite unfortunate, but you ran out of tries. The word was " + word + ", Maybe next time though!")

def display_hangman(tries):
    stages = [ """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
                """,
                """
                 --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
                """,
                """
                --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     
                  -
                """,
                """
                --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |
                  -
                """,
                """
                --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
                """,
                """
                --------
                  |      |
                  |      O
                  |     
                  |      
                  |     
                  -
                """,
                """
                --------
                  |      |
                  |      
                  |     
                  |     
                  | 
                  -
                """
    ]
    return stages[tries]

def main():
  word = get_word()
  play(word)
while input ("Would you like to play again? (Y/N) ").upper() == "Y":
  word = get_word()
  play(word)

if __name__ == "__main__":
  main()
#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
