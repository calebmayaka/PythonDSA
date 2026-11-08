
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            # target is in the right half
            low = mid + 1
        else:
            # target is in the left half
            high = mid - 1

    # target not found
    return -1


# finds the FIRST occurrence of target when the list has duplicates
def binary_search_first(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            result = mid
            # keep searching the left half for an earlier match
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print(binary_search(numbers, 13))  # 6
    print(binary_search(numbers, 1))   # 0
    print(binary_search(numbers, 19))  # 9
    print(binary_search(numbers, 4))   # -1 (not in list)
    print(binary_search([], 5))        # -1 (empty list)

    duplicates = [1, 2, 2, 2, 3, 4]
    print(binary_search_first(duplicates, 2))  # 1

if __name2__ == "__"
