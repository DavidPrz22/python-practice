def main():
    shoes = [ {"type": "I", "size": 38}, {"type": "R", "size": 38}, {"type": "R", "size": 42}, {"type": "I", "size": 41}, {"type": "I", "size": 42} ]

    print(organize(shoes))


def organize(shoes):
    organized = []
    paired = []

    for i in range(len(shoes)):

        for j in range(i + 1, len(shoes)):

            if shoes[i]["size"] == shoes[j]["size"]:

                first_index = i
                second_index = j

                if (
                    (shoes[i]["type"] == "I" and shoes[j]["type"] == "R")
                    or (shoes[i]["type"] == "R" and shoes[j]["type"] == "I")
                ) and (not (first_index in paired) and not (second_index in paired)):

                    organized.append(shoes[i]["size"])
                    paired.extend([first_index, second_index])
                    break
    
    return organized


if __name__ == "__main__":
    main()
