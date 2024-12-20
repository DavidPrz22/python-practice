import sys
import re

def main():

    print(validate(sys.argv[1]))


def validate(ip):
    if valid := re.search(r"^(?:[0-9]\.|[1-9][0-9]\.|1[0-9][0-9]\.|2[0-5][0-5]\.){3}([0-9]|[ 1-9][0-9]|1[0-9][0-9]|2[0-5][0-5])$", ip.strip()):
        return "valid"
    
    return "invalid"


if __name__ == "__main__":
    main()