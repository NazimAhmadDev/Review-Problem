import random

chance = 5

print(f"You have {chance} chances")
print()

while chance != 0:
    try:
        a = int(input("Enter the lower range : "))
        b = int(input("Enter the higher range : "))

        if a > b:
            raise ValueError("Lower range should be lesser than higher range value")
    
        random_num = random.randrange(a,b)

        guessed_num = int(input("Enter the guessed number : "))

        if guessed_num == random_num:
            print("You Win!!!")
            chance -= 1
            print()
            break
            #print(f"You have {chance} chance left")

        elif guessed_num > random_num:
            print(f"Your guessed number {guessed_num} is greater than {random_num}")
            chance -= 1
            print()
            print(f"You have {chance} chance left")

        else:
            print(f"Your guessed number {guessed_num} is lesser than {random_num}")
            chance -= 1
            print()
            print(f"You have {chance} chance left")
    
    except ValueError as e:
        print(f"Error : {e}")
        print()
        print(f"You have {chance} chance")

print("Game Over!!!")
