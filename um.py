import sys
import re

def main():
    string = input("Input: ")
    print(count(string))


def count(um):
    
    if valid := re.findall(r"\b(um,|, um,|um....)", um.strip(), re.IGNORECASE):
        
        return len(valid)
    
    return 0


if __name__ == "__main__":
    main()