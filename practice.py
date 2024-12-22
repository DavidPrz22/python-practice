def main():
    size = 5

    height = (size * 2) - 1
    width = (height * 2) - 1

    middle_width = round(width / 2 - 1)
    middle_height = round(height / 2 - 1)

    rangoli = [["-"] * width for _ in range(height)]
    letters = ["e", "d", "c", "b", "a"]

    for index in range(size):
        expand = 0
        for i in range(height): 
            for j in range(width):

                if j == middle_width - expand or j == middle_width + expand:
                    rangoli[index + i][j] = letters[index]

            if i + index == height - 1 - index:
                break
            elif i + index < middle_height:
                expand += 2
            elif i + index >= middle_height:
                expand -= 2

    for row in rangoli:
        for i in row:
            print(i, end="")
        print()


if __name__ == "__main__":
    main()
