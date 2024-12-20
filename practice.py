import math

def main():
    string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"

    wrapping_index = 4
    wrapper_string = []
    wrapping_length = math.ceil(len(string) / wrapping_index)

    left = 0
    right = wrapping_index

    while True:

        temp = string[left:right]
        if not temp:
            break

        wrapper_string.append(temp)
        left += wrapping_index
        right += wrapping_index

    for i in wrapper_string:

        print(i)


if __name__ == "__main__":
    main()