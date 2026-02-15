import random
import statistics

# Dataset
data = [12, 15, 14, 10, 18, 21, 13, 16, 19, 17]

# 1. Z-Score Calculation
mean_val = statistics.mean(data)
std_dev = statistics.stdev(data)

z_scores = [(x, (x - mean_val) / std_dev) for x in data]
outliers = [x for x, z in z_scores if abs(z) > 2]

# 2. Probability Simulation

# Coin Toss Simulation
coin_tosses = [random.choice(['Heads', 'Tails']) for _ in range(1000)]
prob_heads = coin_tosses.count('Heads') / 1000
prob_tails = coin_tosses.count('Tails') / 1000

# Dice Roll Simulation
dice_rolls = [random.randint(1, 6) for _ in range(1000)]
dice_probs = {i: dice_rolls.count(i) / 1000 for i in range(1, 7)}

# 3. Conditional Probability
# Example: Probability of passing if value >= mean
pass_count = sum(1 for x in data if x >= mean_val)
total_count = len(data)
cond_prob = pass_count / total_count

# Output
print(f"Dataset: {data}\n")
print(f"Mean: {mean_val:.2f}")
print(f"Std Dev: {std_dev:.2f}\n")

print("Z-Scores:")
for val, z in z_scores:
    print(f"{val} → {z:.2f}")
print(f"\nOutliers: {outliers}\n")

print("Coin Toss Probability:")
print(f"Heads: {prob_heads:.3f}")
print(f"Tails: {prob_tails:.3f}\n")

print("Dice Probability:")
for face, prob in dice_probs.items():
    print(f"{face}: {prob:.3f}")

print(f"\nConditional Probability (Pass | ≥ Mean): {cond_prob:.3f}")
