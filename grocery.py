def main():

    grocery_list = []
    item_count = []
    while True:
        try:
            grocery_list.append(input().strip().upper())
        except EOFError:

            grocery_list.sort()
            for i in grocery_list:

                count = grocery_list.count(i)

                if not i in [key["item"] for key in item_count]:
                    item_count.append({"item": i, "count": count})

            grocery_items = sorted(set(grocery_list))

            for (i, item) in enumerate(grocery_items):
                print(f"{item_count[i]["count"]}. {item}")
            
            break
main()