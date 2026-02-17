def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    steps = []

    while left <= right:
        mid = left + (right - left) // 2
        steps.append(arr[mid])

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps


# Take user input
print("Enter sorted numbers separated by space:")
user_input = input()

# Convert input string to list of integers
numbers = list(map(int, user_input.split()))

print("Enter the number to search:")
target = int(input())

# Call binary search
result, steps = binary_search(numbers, target)

# Output result
print("\n===== Binary Search Result =====")

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")

# Tree side view (professional)
print("\n===== Tree Side View (Search Path) =====")

level = 0
for value in steps:
    print("   " * level + "└── " + str(value))
    level += 1

"""
What is Binary Search?

Binary Search is an efficient searching algorithm used to find a target element in a sorted array or list. 
It works by repeatedly dividing the search interval in half. Instead of checking each element one by one (like linear search), binary search compares the target with the middle element. 
If the target is smaller, it searches the left half; if larger, it searches the right half. This process continues until the element is found or the search space becomes empty. The time complexity of binary search is O(log n), making it significantly faster than linear search (O(n)) for large datasets.

Why Do We Use Binary Search?

We use binary search because it is highly efficient for large, sorted datasets. 
As the dataset size increases, binary search performs dramatically better than linear search since it reduces the search space by half at each step. 
This efficiency is crucial in systems where performance and speed are important, such as databases, search engines, and large-scale data processing systems.

Where is Binary Search Used in AI?

In Artificial Intelligence and Machine Learning, binary search is commonly used in optimization problems, 
hyperparameter tuning (such as searching for optimal learning rates), threshold finding, decision boundary tuning, and search space reduction techniques. 
It is also used internally in algorithms that require sorted data structures, such as nearest neighbor searches, model calibration, and certain tree-based methods like binary search trees. In reinforcement learning and model selection processes, binary search can help efficiently narrow down parameter ranges to achieve optimal performance.

"""