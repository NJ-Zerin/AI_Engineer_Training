def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Take user input
user_input = input("Enter numbers separated by space: ")

# Convert input string to list of integers
arr = list(map(int, user_input.split()))

# Sort the array
sorted_arr = bubble_sort(arr)

# Show output
print("Sorted array:", sorted_arr)



"""
Bubble Sort:
Bubble Sort is a simple way to sort numbers. 
It works by comparing two neighbors and swapping them if the left one is bigger. 
The largest numbers “bubble up” to the end with each pass. Repeat until the whole list is sorted.

Example:
Unsorted list: [5, 3, 8, 4]
Pass 1: [3, 5, 8, 4] → [3, 5, 4, 8]
Pass 2: [3, 5, 4, 8] → [3, 4, 5, 8]
Pass 3: [3, 4, 5, 8] → no swaps → DONE ✅
Sorted list: [3, 4, 5, 8]

Key Points:
In-place → no extra memory
Stable → equal numbers keep order
Best case: O(n) (already sorted)
Worst case: O(n²) (reversed list)
"""

