def main():
    
    date_input = input("Date: ").strip().split("/")


    while True:
        try:
            for i in range(len(date_input)):
                date_input[i] = int(date_input[i])

            if date_input[0] and date_input[1] > 9:
                print(f"{date_input[2]}-{date_input[0]}-{date_input[1]}")
            elif date_input[0] and date_input[1] < 10:
                print(f"{date_input[2]}-0{date_input[0]}-0{date_input[1]}")
            elif date_input[0] > 9 and date_input[1] < 10:
                print(f"{date_input[2]}-{date_input[0]}-0{date_input[1]}")
            else:
                print(f"{date_input[2]}-0{date_input[0]}-{date_input[1]}")
        except ValueError:
            date_input = input("Date: ").strip().split("/")
        else:
            break

main()