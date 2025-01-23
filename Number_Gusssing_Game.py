import random


cnt = 5

print(f"You have a total of -->{cnt} chances")


while cnt != 0:
    try:
        lower_range = int(input("Enter the Lower range : "))
        upper_range = int(input("Enter the Upper Range : "))

        if upper_range<lower_range:
            raise ValueError("Your lower range should always be smaller than upper range")
    
        random_num = random.randrange(lower_range,upper_range)

        guessed_num = int(input(f"Enter the guessed number between the range ---> {lower_range} and ---> {upper_range} : "))

        if guessed_num == random_num:
            print("Congrats you have won")
            cnt -= 1
            print()
            break

        elif guessed_num > random_num:
            print(f"Your guessed number ---> {guessed_num} is greater than ---> {random_num}")
            cnt -= 1
            print()
            print(f"You have {cnt} chance left")

        else:
            print(f"Your guessed number {guessed_num} is lesser than {random_num}")
            cnt -= 1
            
            print(f"You have a total of --->{cnt} chances left")
    
    except ValueError :
        print(f"Error encountered ---> : {ValueError}")
       
        print(f"You have only --->{cnt} chance left")

