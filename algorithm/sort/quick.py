# 快速排序
def sort_quick(arr):
    if len(arr) is 0:
        return arr

    left = []
    right = []
    middle_digit_index = int(len(arr) / 2)
    middle_digit = arr[middle_digit_index]

    for i in range(len(arr)):
        if i is middle_digit_index:
            continue
        if arr[i] < middle_digit:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return sort_quick(left) + [middle_digit] + sort_quick(right)
