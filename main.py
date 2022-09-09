import random
import string
from words import words
from visuals import visualList


def chooseWord():
    return words[random.randint(0, (len(words) - 1))].lower()


def Hangman():
    lifeCount: int = 7

    word = chooseWord()

    wordLetters = set(word)  # used to keep track what remains
    usedLetters = set();    #track the letters already inputted
    alphabet = set(string.ascii_lowercase)  # have a list of the alphabet (in lower case) to compare if input is valid

    while lifeCount > 0 and len(wordLetters) > 0:
        #output current word status
        wordList = [letter if letter in usedLetters else '-' for letter in word]

        print("Current Life Count: ", lifeCount)
        print("Used letters: ", ' '.join(usedLetters))
        print("Current word: ", " ".join(wordList))
        print(visualList[lifeCount])
        userInput = input("Guess a letter: ").lower()

        #if the user inputted letter is in the alphabet and not in the usedletter's list
        if userInput in alphabet - usedLetters:
            usedLetters.add(userInput)
            if userInput in wordLetters:
                wordLetters.remove(userInput)
            else:
                lifeCount -= 1
                print("The letter you inputted, ", userInput, " is not in the word.")

        elif userInput in usedLetters:
            print("you already used the letter, ", userInput, ". Try again.")
        else:
            print("Input not valid. Try again.")

    if lifeCount == 0:
        print("Game Over. The word was, ", word, ".")
        print(visualList[0])

    else:
        print("You won!")


Hangman()
