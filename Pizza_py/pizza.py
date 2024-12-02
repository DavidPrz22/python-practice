import csv
import sys
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("too few arguments")

    if len(sys.argv) > 2:
        sys.exit("too many arguments")
    
    if not sys.argv[1].endswith(".csv"):
        sys.exit("not a .csv file")
    
    sicilian_menu = []

    try:
        with open(sys.argv[1]) as file:
            sicilian = csv.DictReader(file)
            for row in sicilian:
                sicilian_menu.append(row)
    except Exception as err:
        print(err)
        
    diction = {}

    for key in sicilian_menu[0].keys():
        diction.update({key : [item[key] for item in sicilian_menu]})

    print(tabulate(sicilian_menu, headers="keys", tablefmt="grid"))
    print(tabulate(diction, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()