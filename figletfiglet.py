from pyfiglet import Figlet
from sys import argv
def main():

    if len(argv) == 3:

        if not(argv[1] == "--font" or argv[1] == "-f"):
            print("USAGE: --font/-f [STYLE]")
            return

        f = Figlet(font=argv[2])
    else:
        f = Figlet(font="slant")

    text = input("Input: ")
    print(f"Output:\n {f.renderText(text)}")


if __name__ == "__main__":
    main()