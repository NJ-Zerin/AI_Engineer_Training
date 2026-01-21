# 1. Take input from the user
numbers = input("Enter numbers separated by commas: ")  

# 2. Convert the input string into a list of integers
# .split(",") splits the string at commas 
# int(num) converts each string number to an integer 
numbers_list = [int(num) for num in numbers.split(",")]  

# 3. Calculate total number of values 
total_values = len(numbers_list)

# 4. Calculate minimum and maximum values
minimum_value = min(numbers_list)
maximum_value = max(numbers_list)

# 5. Calculate mean (average)
mean_value = sum(numbers_list) / total_values

# 6. Print a clean summary
print("\n===== Data Summary =====")
print("Total values   :", total_values)
print("Minimum value  :", minimum_value)
print("Maximum value  :", maximum_value)
print("Mean value     :", f"{mean_value:.2f}")