import random

#get user to input number that will be the top of range
topOfRange = input("Type a number: ")


#check to see if user entered a number, if true make that number topOfRange
if topOfRange.isdigit():
    topOfRange = int(topOfRange)

    #check if number is less than or equal to zero
    if topOfRange <= 0:
        print("Please enter a number larger than Zero.")
        quit()
#this will run if user did not enter a number
else:
      print("Please enter a valid number next time.")
      quit()

#generate random number
randomNumber = random.randint(0, topOfRange)

#explain game to user
print("Wonderful! Now you will guess a number from 0 to" ,  topOfRange)

#Create a variable that will count the number of guesses a user makes
guesses = 0

while True:
    #increment guesses variable each time loop is restarted
    guesses += 1
    #allow user to guess number
    userGuess = input("Make a guess: ")
    
    if userGuess.isdigit():
        userGuess = int(userGuess)
    #this will run if user did not enter a valid number
    else:
        print("Please enter a number next time.")
        continue
    
    #run if user guessed correctly
    if userGuess == randomNumber:
        print("Congrats! You guessed Correctly!")
        break
    #run if user guessed to high
    elif userGuess > randomNumber:
        print("You guessed too high!")
    #run if user guessed to high
    else:
        print("You guessed too low!")

print("You guessed correctly in" , guesses , "guesses!")