#Name:Carter Guthrie
#Date:2/22/26
#Assignment:Lab 5
#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns True if letter is anywhere in the word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns True if letter is in the specific spot"""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Capital for right spot, lowercase for wrong spot, * if missing"""
    result = ""
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            result += myGuess[i].upper()
        elif inWord(myGuess[i], word):
            result += myGuess[i].lower()
        else:
            result += "*"
    return result

def main():
    # Load word list
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList).strip().lower()
    
    print("Welcome to Word Game! Guess the 5-letter word.")
    
    # User gets 6 guesses
    for attempt in range(1, 7):
        guess = input(f"Guess {attempt}: ").lower()
        
        feedback = rateGuess(guess, todayWord)
        print(feedback)
        
        if guess == todayWord:
            print("You got it!")
            break
    else:
        print(f"Game over! The word was: {todayWord}")

if __name__ == '__main__':
    main()