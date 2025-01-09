def execute(code: str) -> int:
    value = 0
    i = 0
    code_len = len(code)
    
    # Cache for matching brackets
    bracket_pairs = {}
    stack = []
    
    # Pre-process bracket pairs
    for pos, char in enumerate(code):
        if char == '[':
            stack.append(pos)
        elif char == ']' and stack:
            start = stack.pop()
            bracket_pairs[start] = pos
            bracket_pairs[pos] = start

    while i < code_len:
        char = code[i]
        
        match char:
            case '+':
                value += 1
            case '-':
                value -= 1
            case '[':
                if value == 0:
                    i = bracket_pairs[i]
            case ']':
                if value != 0:
                    i = bracket_pairs[i]
            case '{':
                if value == 0:
                    # Skip to matching '}'
                    depth = 1
                    while depth > 0 and i < code_len - 1:
                        i += 1
                        if code[i] == '{':
                            depth += 1
                        elif code[i] == '}':
                            depth -= 1
            case '>':
                pass
            case '}':
                pass
            case _:
                raise ValueError(f"Invalid instruction: {char}")
        
        i += 1
    
    return value

def main():
    test_cases = [
        '+++',              # 3
        '+--',             # -1
        '>>>+{+-}{-}',     # 0
        '>+++[-]',         # 0
        '{+}{+}{+}',       # 0
        '------[+]++',     # 2
        '+{[-]+}+',        # 2
        '----[+{+}]+{++++}' # 5
    ]
    
    for test in test_cases:
        print(f"{test}: {execute(test)}")

if __name__ == "__main__":
    main()

#     for i in generate_gift_sets(["car", "doll", "ball", "puzzle", "toy", "paddle"]):
#         print(i)


# def generate_gift_sets(toys):

#     result = []
    
#     def generate_combinations(start, current_combo, target_length):

#         if len(current_combo) == target_length:
#             result.append(current_combo[:])
#             return
            
#         for i in range(start, len(toys)):
#             current_combo.append(toys[i])
#             generate_combinations(i + 1, current_combo, target_length)
#             current_combo.pop()
    
#     for length in range(1, len(toys) + 1):
#         generate_combinations(0, [], length)
        
#     return result


    # VERSION 0.0.9 BETA ALPHA PRO LIMITED EDITION 4K ULTRA 240FPS LSS
    # gift_sets = []
    # length = len(sets)

    # # FIRST COMBINATION OF 1
    # for item in range(len(sets)):
    #     gift_sets.append([sets[item]])

    # # COMBINATION FOR MORE THAN ONE ITEMS
    # # STARTS WITH TWO COMBINATIONS UP TO N - 1
    # combinations_quantity = len(sets) - 1
    # factor = 1
    # n = 0
    # i = 0

    # if length > 1:

    #     while n < combinations_quantity:

    #         for j in range(i + 1, length - n):

    #             temp = [sets[i]]

    #             for k in range(factor):

    #                 if j + k in range(length):
    #                     temp.append(sets[j + k])

    #             gift_sets.append(temp)

    #         if (i == length - 2 - n): # tracking i index
    #             n += 1
    #             factor += 1
    #             i = 0
    #         else:
    #             i += 1




    # VERSION 0.0.1
    # for i in range(length + 1):

    #     if i < length:
    #         for j in range(i, length):

    #             temp_set = []

    #             if i > 0:
    #                 temp_set.append(sets[i - 1])
    #                 temp_set.append(sets[j])
    #             else:
    #                 temp_set.append(sets[j])
            
    #             gift_sets.append(temp_set)
    #     else:
    #         gift_sets.append(sets)
    