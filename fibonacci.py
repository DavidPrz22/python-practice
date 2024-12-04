import sys

def main():

    for i in fibonacci(int(sys.argv[1])):
        print(i)


def fibonacci(sequence):
    listst = list(range(sequence))
    for i in listst:
    
        if i == 0:
            first_number = 0
            second_number = 1
        else:
            yield second_number
            temp = second_number
            second_number = first_number + second_number
            first_number = temp
    


if __name__ == "__main__":
    main()