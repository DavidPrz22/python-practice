def main():

    print(fixPackages('abc(def(gh)i)jk'))
    # // ➞ "abcde"
    # // Volteamos "cb" dentro de los paréntesis

    # fixPackages('a(bc(def)g)h')
    # # // ➞ "agdefcbh"
    # # // 1º volteamos "def" → "fed", luego volteamos "bcfedg" → "gdefcb"

    # fixPackages('abc(def(gh)i)jk')
    # # // ➞ "abcighfedjk"
    # # // 1º volteamos "gh" → "hg", luego "defhgi" → "ighfed"

    # fixPackages('a(b(c))e')
    # # // ➞ "acbe"
    # # // 1º volteamos "c" → "c", luego "bc" → "cb"

def fixPackages(string: str, index: int=0):

    open_parenthesis = None
    found = False
    restart = True
    length = len(string)

    while restart == True:
        restart = False
        for i in range(length - index):
            if string[i + index] == "(":

                open_parenthesis = i + index
                string = fixPackages(string, i + index + 1)

                if len(string) != length:
                    length = len(string)
                    restart = True
                    break
            elif isinstance(open_parenthesis, int) and string[i + index ] == ")":

                close_parenthesis = i + index
                found = True
                break

    if found:
        string_range = string[open_parenthesis + 1: close_parenthesis]
        reveresed_string = reverseString(string_range)

        parenthesis_range = string[open_parenthesis: close_parenthesis + 1]
        return string.replace(parenthesis_range, reveresed_string)
    else:
        return string

def reverseString(string: str):
    reversed_string = ""

    for char in string[::-1]:
        reversed_string += char
    
    return reversed_string


if __name__ == "__main__":
    main()
