import csv

def main():

    names_before = []

    try:
        with open("before.csv") as file:
            rows = csv.DictReader(file)
            for row in rows:
                names_before.append(row)
    except Exception as error:
        print(error)

    try:

        with open("after.csv", "w") as file:
            new_file = csv.DictWriter(file, fieldnames=["First Name","Last Name", "House"])
            new_file.writeheader()

            for row in names_before:
                first_name, last_name = row["name"].rstrip().split(',')

                new_file.writerow({"First Name": first_name, "Last Name": last_name, "House": row['house']})

    except Exception as error:
        print(error.with_traceback)

    
if __name__ == "__main__":
    main()