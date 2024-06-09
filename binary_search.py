"""Module providing a function implementing binary search"""
def binary_search(arr, target):
    """Function implementing binary search"""
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if low < len(arr):
        upper_bound = arr[low]
    else:
        upper_bound = float('inf')

    return (iterations, upper_bound)

# Тестування функції
sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5]
print(binary_search(sorted_array, 3.3))  # Виведе: (3, 3.3)
print(binary_search(sorted_array, 6.6))  # Виведе: (3, inf)
print(binary_search(sorted_array, 4.0))  # Виведе: (3, 4.4)
