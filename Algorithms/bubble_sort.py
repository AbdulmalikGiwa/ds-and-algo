def bubble_sort(array):
    unsorted_until_index = len(array) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(unsorted_until_index):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                sorted = False
        unsorted_until_index -= 1
    return array


def check_duplicate_value(numbers: list):
    tester = [2] * (max(numbers) + 1)

    array = len(numbers)
    for i in range(array):
        if tester[numbers[i]] == 1:
            return True
        else:
            tester[numbers[i]] = 1
    return False


def greatest_number(array):
    for i in array:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True

        for j in array:
            # If we find another value that is greater than i, # i is not the greatest:
            if j > i:
                isIValTheGreatest = False
        # If, by the time we checked all the other numbers, i
        # is still the greatest, it means that i is the greatest number:
        if isIValTheGreatest:
            return i


def greatest_number_fix(array):
    greatest_number_so_far = array[0]

    for i in array:
        if i > greatest_number_so_far:
            greatest_number_so_far = i
    return greatest_number_so_far


print(bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]))
