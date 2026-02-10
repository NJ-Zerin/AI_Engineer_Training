import math
from collections import Counter

# Dataset
data = [12, 15, 14, 10, 18, 21, 13, 16, 19, 17]

# ---------- Helper Functions ----------

def mean(dataset):
    return sum(dataset) / len(dataset)

def median(dataset):
    sorted_data = sorted(dataset)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def mode(dataset):
    counts = Counter(dataset)
    max_freq = max(counts.values())

    if max_freq == 1:
        return None  # No mode
    return [value for value, freq in counts.items() if freq == max_freq]

def data_range(dataset):
    return max(dataset) - min(dataset)

def variance(dataset):
    m = mean(dataset)
    return sum((x - m) ** 2 for x in dataset) / len(dataset)

def standard_deviation(dataset):
    return math.sqrt(variance(dataset))

def five_number_summary(dataset):
    sorted_data = sorted(dataset)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid:]
    else:
        lower_half = sorted_data[:mid]
        upper_half = sorted_data[mid + 1:]

    return {
        "Min": min(sorted_data),
        "Q1": median(lower_half),
        "Median": median(sorted_data),
        "Q3": median(upper_half),
        "Max": max(sorted_data)
    }

def detect_outliers(dataset):
    summary = five_number_summary(dataset)
    q1 = summary["Q1"]
    q3 = summary["Q3"]
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    return [x for x in dataset if x < lower_bound or x > upper_bound]

# ---------- Calculations ----------

mean_value = mean(data)
median_value = median(data)
mode_value = mode(data)
range_value = data_range(data)
variance_value = variance(data)
std_dev_value = standard_deviation(data)
summary = five_number_summary(data)
outliers = detect_outliers(data)

# ---------- Output ----------

print(f"Dataset: {data}")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Range: {range_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}\n")

print("5 Number Summary:")
print(f"Min: {summary['Min']}")
print(f"Q1: {summary['Q1']}")
print(f"Median: {summary['Median']}")
print(f"Q3: {summary['Q3']}")
print(f"Max: {summary['Max']}\n")

print(f"Outliers: {outliers}")

