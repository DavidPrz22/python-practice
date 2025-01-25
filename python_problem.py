def main():

    generate_gift_sets(["car", "doll", "ball", "puzzle", "toy"])


def generate_gift_sets(toys):

    result = []

    def generate_combinations(start, current_combo, target_length):

        if len(current_combo) == target_length:
            result.append(current_combo[:])
            return

        for i in range(start, len(toys)):
            current_combo.append(toys[i])
            generate_combinations(i + 1, current_combo, target_length)
            current_combo.pop()

    for length in range(1, len(toys) + 1):
        generate_combinations(0, [], length)

    return result


if __name__ == "__main__":
    main()


# def find_combinations(combinations_list: list):
#     length = len(combinations_list)
#     result = []

#     for index in range(length):

#         for idx in range(0, length - index):

#             nexted = idx + 1
#             for ind in range(nexted, length - index):

#                 selected_item = [combinations_list[idx]]

#                 for indx in range (ind, ind + index):

#                     selected_item.append(combinations_list[indx])

#                 if selected_item not in result:
#                     result.append(selected_item)

#     results = []

#     for element_comb in result:

#         element = element_comb[len(element_comb) - 1]
#         cycle_lenth = length - (combinations_list.index(element) + 1)

#         index_append_start = combinations_list.index(element) + 1

#         for i in range(cycle_lenth):
#             comb_copy = element_comb.copy()
#             for j in range(index_append_start + i, length):
#                 comb_copy.append(combinations_list[j])
#                 results.append(comb_copy)
#                 break
    
#     results = [[i] for i in combinations_list] + results
#     for d in results:
#         print(d)



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