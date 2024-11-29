def main():

    grocery_list = []
    item_count = []
    while True:
        try:
            grocery_list.append(input().upper())
        except EOFError:

            for i in grocery_list:

                count = grocery_list.count(i)
                
                if not i in [subkey for key in item_count for subkey in key.values()]:
                    item_count.append({"item": i, "count": count})

            grocery_items = set(grocery_list)
            
            for (i, item) in enumerate(grocery_items):
                print(f"{item_count[i]["count"]}. {item}")

main()