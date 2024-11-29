def main():

    grocery_list = []
    item_count = {}
    while True:
        try:
            grocery_list.append(input().strip().upper())
        except EOFError:

            grocery_list.sort()
            for grocery in grocery_list:
                count = grocery_list.count(grocery)

                if not item_count.get(grocery):
                    item_count[grocery] = count
            
            for item in item_count:
                print(f"{item_count[item]} {item}")
            
            break


main()