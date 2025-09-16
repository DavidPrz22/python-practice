from support_sql import Database

def main():

    db = Database("./mydatabase.db")

    for user in db.db_fetch("SELECT * FROM Users"):
        print(user)


if __name__ == "__main__":
    main()