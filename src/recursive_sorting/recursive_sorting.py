import random
n = list(range(20))
random.shuffle(n)
print(n)

# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arr1, arr2):
    results = []
    i = 0
    j = 0
    while len(arr1) > i and len(arr2) > j:
        if arr1[i] >= arr2[j]:
            results.append(arr2[j])
            j += 1
        else:
            results.append(arr1[i])
            i += 1
    results += arr1[i:]
    results += arr2[j:]
    return results


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    halfway = len(arr) // 2
    left = merge_sort(arr[:halfway])
    right = merge_sort(arr[halfway:])

    return merge(left, right)


print(merge_sort(n))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
