def binary_search(array: list, search_value: int):
    lower_bound = 0
    upper_bound = len(array) - 1

    while lower_bound < upper_bound:
        mid_index = int((lower_bound + upper_bound)/2)

        mid_value = array[mid_index]

        if search_value == mid_value:
            return mid_index
        elif search_value < mid_value:
            upper_bound = mid_index - 1
        elif search_value > mid_value:
            lower_bound = mid_index + 1

    return None


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20))
