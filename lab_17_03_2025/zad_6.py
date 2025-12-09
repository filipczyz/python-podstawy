def process_lists(list1, list2):

    combined_list = list1 + list2
    unique_list = list(set(combined_list))

    cubed_list = [x ** 3 for x in unique_list]

    return cubed_list

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = process_lists(list1, list2)

print(result)