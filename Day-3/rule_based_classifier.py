# Take input from the user and convert it to lowercase
# This avoids case-sensitivity issues during matching
text = input("Enter text: ").lower()

# Split the text into individual words and convert them into a set
# Using a set removes duplicates and makes keyword matching faster
words = set(text.split())

# Dictionary that defines categories and their related keywords
# Key   -> category name
# Value -> set of keywords associated with that category
categories = {
    "technology": {"python", "ai", "computer", "software"},
    "sports": {"football", "cricket", "tennis", "basketball"},
    "education": {"school", "college", "study", "exam"}
}

# Dictionary to store how many keywords match for each category
# Example: {"technology": 2, "sports": 0, "education": 1}
scores = {}

# Loop through each category and its keywords
for category, keywords in categories.items():
    # Find common words between user input and category keywords
    # Set intersection (&) returns matching keywords
    # len() counts how many keywords matched
    scores[category] = len(words & keywords)

# Select the category with the highest number of matches
# max() uses scores.get to compare dictionary values
best_category = max(scores, key=scores.get)

# If no keywords matched in any category, label it as Unknown
if scores[best_category] == 0:
    print("Predicted Category: Unknown")
else:
    # Otherwise, print the category with the highest match count
    print("Predicted Category:", best_category)
