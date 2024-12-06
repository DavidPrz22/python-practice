import sys

def main():

    for i in fibonacci(int(sys.argv[1])):
        print(i)


def fibonacci(sequence):
    result = []
    for i in range(sequence):
    
        if i == 0:
            first_number = 0
            second_number = 1
        else:
            result.append(second_number)
            temp = second_number
            second_number = first_number + second_number
            first_number = temp
    return result


if __name__ == "__main__":
    main()