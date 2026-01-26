import csv
import statistics
import pandas as pd
import os  # for file paths


# ---------- STEP 1: LOAD DATA (Dataset Loading) ----------

def load_data(filepath):
    """
    Loads numeric data from TXT, CSV, or Excel files
    Ignores non-numeric values
    Returns a list of integers
    """

    numbers = []

    try:
        # TXT file
        if filepath.endswith(".txt"):
            file = open(filepath, "r")
            for line in file:
                line = line.strip()
                if line.isdigit():              # check numeric
                    numbers.append(int(line))
            file.close()

        # CSV file
        elif filepath.endswith(".csv"):
            file = open(filepath, "r")
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].isdigit():    # check numeric
                    numbers.append(int(row[0]))
            file.close()

        else:
            print("Unsupported file format")

    except FileNotFoundError:
        print("Error: File not found.")

    except ValueError:
        print("Error: File contains invalid data.")

    return numbers


# ---------- STEP 2: PROCESS DATA (Preprocessing) ----------

def analyze_data(numbers):
    """
    Performs basic statistical analysis
    """

    if len(numbers) < 2:
        print("Not enough numeric data to analyze.")
        return None

    return {
        "numbers": numbers,
        "count": len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "mean": sum(numbers) / len(numbers),
        "median": statistics.median(numbers),
        "std_dev": statistics.stdev(numbers)
    }


# ---------- STEP 3: DISPLAY RESULTS ----------

def show_results(results):
    if results is None:
        return

    print("\n----- Data Analysis Summary -----")
    print("Numeric Values     :", results["numbers"])
    print("Total Count        :", results["count"])
    print("Minimum Value      :", results["min"])
    print("Maximum Value      :", results["max"])
    print("Mean (Average)     :", round(results["mean"], 2))
    print("Median             :", results["median"])
    print("Standard Deviation :", round(results["std_dev"], 2))


# ---------- MAIN PIPELINE ----------

def main():
    # Get user input
    filename = input("Enter dataset filename (.txt / .csv / .xlsx): ").strip()

    # Automatically make it path-independent
    script_dir = os.path.dirname(os.path.abspath(__file__))  # folder of this script
    filepath = os.path.join(script_dir, filename)            # full path

    data = load_data(filepath)       # Load dataset
    results = analyze_data(data)     # Process dataset
    show_results(results)            # Output results


main()
