import random

attempts = 0
random_num = random.randint(1,100)
while True:
    user_input = int(input("Guess the number 1 to 100: "))
    attempts +=1
    if user_input > random_num:
        print(f"Your guess is too high! This was your attempt number {attempts}")
    elif user_input < random_num:
        print(f"Your guess is too low! This was your attempt number {attempts}")
    elif user_input > 100:
        print(f"You have to stay in 100 range! This was your attempt number {attempts}")
    elif user_input < 0:
        print(f"Your guess should not be lower than 0! This was your attempt number {attempts}")
    elif user_input == random_num:
        print(f'You found it in {attempts} attempts! It was {random_num}!!!')
        try_again = input("Do you wanna try again? Yes or NO ==> ")
        if try_again == "Y" or try_again == "YES" or try_again == "Yes" or try_again == "yes" or try_again == "ok":
            attempts = 0
            continue
        else:
            break
    elif attempts >= 10:
        print(f'You lost! You have attempted {attempts} times!')
        if try_again == "Y" or try_again == "YES" or try_again == "Yes" or try_again == "yes" or try_again == "ok":
            attempts = 0
            continue
        else:
            break