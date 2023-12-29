# This is a sample Python script.
import random
import time


############################################
# Return Random sentence
############################################
def RandomSentenceList():
    listOfWord = [["Act","as","if"], ["Act","without","expectation"], ["All","is","well"],["Be","here","now"]]
    randomWord = random.choice(listOfWord)
    return randomWord

############################################
# Check if List of sentences contains a char
############################################
def IsCharInList(sentenceList,charToCheck):
    if len(charToCheck) == 1 and charToCheck.isalpha():
        for word in sentenceList:
            if charToCheck.lower() in word.lower():
                return True
        return False
    else:
        print("Input Error. not a Char !!!")
        return False


############################################
# Create Guesses List
############################################
def CreateGuessesList(sentenceList,correctGuesses):
    index = 0
    newGuessList =[]
    while index < len(sentenceList):
        word = sentenceList[index]
        newWord = ""
        # iterate on every char in the word
        for char in word:
            if (char.lower() in correctGuesses.lower()):
                newWord += char
            else:
                newWord += "_"
        newGuessList.append(newWord)
        index += 1
    return newGuessList

if __name__ == '__main__':

    print("\nWelcome to My Game. Please try to guess the words \n")

    # List lottery
    sentenceList = RandomSentenceList()

    # Start
    finish = False
    correctGuesses = ""
    score = 0

    # Record the starting time
    startTime = time.time()

    newGuessList = CreateGuessesList(sentenceList, correctGuesses)
    print(newGuessList)

    # Guess Character
    while (not finish):
        charInput = input("Enter a character: ")
        charInList = IsCharInList(sentenceList,charInput)
        if (charInList):
            score += 5  # add 5 points to score on each correct guess
            correctGuesses += charInput
            newGuessList = CreateGuessesList(sentenceList,correctGuesses)
            print(newGuessList)
        else:
            if (score >0): # Only if score is not zero decrement one point
                score -= 1

            print("Wrong !!!  Try Again")

        finish = (sentenceList == newGuessList)

    # Record the ending time
    endTime = time.time()

    # Calculate the elapsed time
    elapsedTime = endTime - startTime

    # if player ended the game less than 30 sec then add bonus 100 Points
    if (elapsedTime <30):
        score += 100

    print (f"\nGood Job - Your score is {score}")

