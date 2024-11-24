def solve(n, k, treasures):
    # Create an array to store treasure values, initialize with 1 for all ids
    max_id = max(t[0] for t in treasures)  # Maximum id in the input
    treasure_values = [1] * (max_id + 1)  # Initialize all treasure ids with value 1
    
    # Update treasure values for the given ids
    for treasure_id, value in treasures:
        treasure_values[treasure_id] = value

    # Sliding window to find the maximum sum and the starting index
    current_sum = sum(treasure_values[:k])  # Initial window sum
    max_sum = current_sum
    best_start = 0
    
    # Slide the window
    for i in range(1, max_id - k + 2):  # Ensure the window fits
        current_sum = current_sum - treasure_values[i - 1] + treasure_values[i + k - 1]
        if current_sum > max_sum or (current_sum == max_sum and i < best_start):
            max_sum = current_sum
            best_start = i

    # Return the result
    return [max_sum, best_start]

# Input handling
n = int(input())  # Number of unique treasures
k = int(input())  # Length of the interval
treasures = [list(map(int, input().split())) for _ in range(n)]  # Treasure ids and values

# Solve and print the result
result = solve(n, k, treasures)
print(result)