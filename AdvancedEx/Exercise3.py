import random
print("Let's play a number guessing game with me\n")
print("What's your name?\n")
playerName=input()
count=1
guessNumber=-1
limit=5
playAgain='YES'
ansNumber=random.randint(1,30)
print("Nice to meet you, "+playerName+", I have a number between 1 and 30. Guess it\n")

while playAgain=='YES':
    print(limit,"You only have to guess 5 times")
    while count<=limit and guessNumber!=ansNumber:
        guessNumber=int(input("Please enter the guesses number -->"))
        if guessNumber==ansNumber:
            break
        elif guessNumber<ansNumber:
            print("The guessed number is less than the number with the computer.")
        else:
            print("The guessed number is greater than the number with the computer.")
        count=count+1
    if guessNumber == ansNumber:
        print(count, "I got it right once!! Congratulations\n")
        if limit>1:
            limit=limit-1
    else:
        print("The number of computer is", ansNumber)
        limit=limit+1
    playAgain=input("Shall we play the game again? (YES or NO)\n")
    count=1
    guessNumber=-1
