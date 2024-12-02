import sys

def main():

    if len(sys.argv) < 2:
        sys.exit("too few command line arguments")
    elif len(sys.argv) > 2:
        sys.exit("too many command line arguments")
    
    file_length = len(sys.argv[1])
    if sys.argv[1][file_length - 3 : file_length] != ".py":
        sys.exit("Must be a python (.py) file")

    with open(sys.argv[1]) as file:

        file_lines = file.readlines()


    # update file_lines
    # get rid of \n character and blankspaces
    for (i, line) in enumerate(file_lines):
        file_lines[i] = line.strip()
        
    total_lines_in_file = len(file_lines)

    blank_lines_count = file_lines.count("")
    total_comments = sum(line[0:1] == "#" for line in file_lines)
        
    total_doc = 0
    open_docstring = None
    close_docstring = None

    for (i, line) in enumerate(file_lines):
        if line.count('"""') > 1:
            total_doc += 1

        elif type(open_docstring) != int and line.count('"""') == 1:
            open_docstring = i
        
        elif '"""' in line:

            close_docstring = i + 1
            total_doc += (close_docstring - open_docstring)
            
            open_docstring = None
            close_docstring = None

    total_lines = total_lines_in_file - blank_lines_count - total_comments - total_doc
    print(total_lines)


if __name__ == "__main__":
    main()