

# import random
# count=0
# while count<3:
#         computer_number = random.randrange(1, 2)
#         user_number = int(input('Please type a number: '))
#
#         if user_number>2:
#                 print('Invalid guess number')
#                 print('Please try! again')
#         elif user_number==count:
#                 print('game over')
#         elif user_number > computer_number:
#                 print('User guess number is', user_number)
#                 print('Computer guess number is', computer_number)
#                 print('"Have one more try".User guess number is too high')
#         elif user_number < computer_number:
#                 print('User guess number is', user_number)
#                 print('Computer guess number is', computer_number)
#                 print('"Have one more try".User guess number is too low')
#         else:
#                 print('User guess number is', user_number)
#                 print('Computer guess number is', computer_number)
#                 print('you guessed it')
#                 break
#         count+=1
#         print('it tooks', count, 'guesse\'s')



#This is a guess the number game.
import random


print("Hello!")


myName=input("Enter Your name: ")
print("\nWelcome, " + myName)
choice="yes"
score=0
while(True):
        if(choice=="no"):
                break
        upper=int(input("Enter lower range: "))
        lower=int(input("Enter upper range: "))
        guessesTaken = 0
        number = random.randint(upper,lower)
        while guessesTaken < 3:
                print("\nTake a guess.")
                guess = input()
                guess = int(guess)

                guessesTaken = guessesTaken + 1

                if guess < number:
                        print("\nHave one more try, Your guess is too low.")
                elif guess > number:
                        print("\nHave one more try, Your guess is too high.")
                else:
                        break

        if guess == number:
                number = str(number)
                print("\nCongrat's")
                score+=5

        else:
                number = str(number)
                print("\nBetter Luck next time")
                print("Score is %d"%score)
                choice=input("Do you want to play again? yes-no :")
