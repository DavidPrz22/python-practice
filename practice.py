def main():

    size = 3

    height = (size * 2) - 1
    width = (height * 2) - 1

    expand = 2
    middle = width/2 - 1
    middle_height = height/2 - 1
    temp = 0

    print(middle)
    for i in range(height): 

        for j in range(width):

            if (j == round(middle) and i == 0) or (j == round(middle) and i == (height - 1)):

                print("a", end="")

            elif (i == round(middle_height)) and (j == round(middle - expand) or j == round(middle + expand) or j == round(middle - expand - 2) or j == round(middle + expand + 2) or j == round(middle)):
                
                print("a", end="")
            
            elif (j == round(middle - expand) or j == round(middle + expand) or j == round(middle)) and i not in (0, height - 1):

                print("a", end="")

            else:
                print("-", end="")


        print()


if __name__ == "__main__":
    main()