taqueria = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    total = 0

    for (item, price) in taqueria.items():
        print(f"{item}: ${price}")

    while True:
        item_selected = input("item: ")
        try:
            if not item_selected:
                print(f"Total: ${total}")
                break

            total = total + taqueria[item_selected]
            print(f"Total: ${total}")
        except KeyError:
            pass




main()