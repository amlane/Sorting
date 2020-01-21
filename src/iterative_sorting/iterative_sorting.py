import random
l = list(range(20))
random.shuffle(l)

# Insertion sort


def insertion_sort(items):
    for i in range(1, len(items)):
        # Store current position in a temp variable
        temp = items[i]
        j = i
        # shift all larger sorted elements to the right by 1
        while j > 0 and temp < items[j-1]:
            # print("j: ", j, "temp:", temp, "item:", items[j-1])
            items[j] = items[j - 1]
            j -= 1
        # insert the element after the first smaller element
        items[j] = temp
    return items


print("Insertion sort: ", insertion_sort(l))


n = list(range(20))
random.shuffle(n)


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        cur_index = i
        smallest_item = None
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        j = i
        while j < len(arr) - 1:
            # if value cur_index > value arr[j] swap values
            if arr[cur_index] > arr[j + 1]:
                smallest_item = arr[j + 1]
                arr[j + 1] = arr[cur_index]
                arr[cur_index] = smallest_item
            j += 1
    return arr


print("Selection Sort: ", selection_sort(n))


# TO-DO:  implement the Bubble Sort function below
m = list(range(20))
random.shuffle(m)


def bubble_sort(arr):
    swap_count = 0
    # loop through the list
    for i in range(0, len(arr)):
        # compare each item to the item to the right
        # if the item to the right is greater than item, swap them and add one to the swap count
        if i < len(arr) - 1 and arr[i] > arr[i + 1]:
            tempVal = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = tempVal
            swap_count += 1
        # if the item to the right is less than or equal to the the item, do nothing
        # once you reach the end of the list if swaps are greater than 0, repeat the loop
        elif i == len(arr) - 1 and swap_count > 0:
            swap_count = 0
            bubble_sort(arr)
    # once swap are 0 return the list
    return arr


print("Bubble sort: ", bubble_sort(m))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
