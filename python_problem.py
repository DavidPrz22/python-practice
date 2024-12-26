def main():

    print(
        inBox([
            "###",
            "#*#",
            "###"
        ])
    ) # ➞ True

    print(inBox([
        "####",
        "#* #",
        "#  #",
        "####"
    ])) # ➞ True
    
    print(inBox([
        "#####",
        "#   #",
        "#  #*",
        "#####"
    ])) # ➞ False

    print(inBox([
        "#####",
        "#   #",
        "#   #",
        "#   #",
        "#####"
    ])) # ➞ False


def inBox(box):
    
    contained = False
    for row in box:
        if "*" in box[0] or "*" in box[-1]:
            return False

        if (not row[0] == "*" and not row[-1] == "*") and "*" in row[1:-1]:
            contained = True

    if contained:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
