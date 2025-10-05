def partition(arr, low, high):
    pivot = arr[low]  # deterministic: first element as pivot
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Original array:", arr)
    deterministic_quicksort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
