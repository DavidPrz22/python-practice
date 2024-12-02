import random
# NEED TO ADD MORE LEVELS

"""
This is 
A
Docstring
"""

def main():
    level = get_level()
    score = 0

    if level == 1:
        for _ in range(0, 5):
        
            first_int = generate_integer(level)
            second_int = generate_integer(level)
            correct_answer = first_int + second_int
            attempts = 3

            while attempts > 0:
                try:
                    answer = int(input(f"{first_int} + {second_int} = "))
                except ValueError:
                    continue

                if answer == correct_answer:
                    score += 10
                    break

                print('EEE')
                attempts -= 1
            else:
                print(f"Answer: {correct_answer}")
    
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            return int(input("Level: "))
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    
    if level == 2:
        return random.randint(10, 20)
    
    if level == 3:
        return random.randint(20, 50)
    
    if level == 4:
        return random.randint(50, 100)


if __name__ == "__main__":
    main()