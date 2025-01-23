# Guess the number game

import random

def play_game():

    '''
        Description: function to play guess the number game

        Parameters: Nothing

        Return: Nothing

    '''

    print("\n----------- Welcome to Guess the Number Game -----------")

    chance = int(input("\nHow many times you want to play?: "))

    while(chance > 0):
            
        try:

            print(f"\nChances left: {chance}")

            lower_range = int(input("\nEnter lower range: "))
            higher_range = int(input("Enter higher range: "))
            
            if(lower_range >= higher_range):
                print(f"\nYour lower range '{lower_range}' is greater than or equal to higher range '{higher_range}'")
                raise Exception
            
            random_number = random.randrange(lower_range + 1, higher_range)

            guessed_number = int(input(f"Guess the number in between {lower_range} and {higher_range}: "))

            if(guessed_number <= lower_range or guessed_number >= higher_range):
                print(f"\nYour guessed number '{guessed_number}' is out of range.")
                raise Exception

            if(guessed_number == random_number):
                print("\nCongratulations, you guessed the number correctly.")
                print("\n----------- Thank You for playing the game -----------\n")
                break

            elif(guessed_number > random_number):
                print(f"\nHard luck, your guessed number '{guessed_number}' is greater than generated random number '{random_number}' ")

            else:
                print(f"\nHard luck, your guessed number '{guessed_number}' is lesser than generated random number '{random_number}' ")

            chance -= 1
            
        except:
            print("\n----------- Please Provide valid Input -----------")

    else:
        print("\n----------- !!! Game Over !!! -----------")
        print("\n----------- Thank You for playing the game -----------\n")


if __name__ == "__main__":
    play_game()




