import random

def main():

    while True:
        try:
            user_number = int(input('Level: '))
            if user_number < 0:
                raise ValueError()
        except ValueError:
            pass
        else:
            break
    
    winning_number = random.randint(1, user_number)

    while True:
        try:
            guess = int(input("Guess: "))

            if guess > winning_number:
                print("Too Large")
            elif guess < winning_number:
                print("Too Small")
            else: 
                print('Just Right!')
                break
        except ValueError:
            pass


if __name__ == "__main__":
    main()