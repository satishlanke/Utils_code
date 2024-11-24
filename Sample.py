def solve(n, k, treasures):
    # Use a dictionary to store the treasure values
    treasure_values = {}
    for treasure_id, value in treasures:
        treasure_values[treasure_id] = value
    
    # Extract all unique ids and sort them
    sorted_ids = sorted(treasure_values.keys())
    
    # Sliding window over the sorted ids
    current_sum = 0
    max_sum = 0
    best_start = -1
    
    # Start of the sliding window
    start = 0
    for end in range(len(sorted_ids)):
        # Add the current id's value to the current sum
        current_sum += treasure_values[sorted_ids[end]]
        
        # Shrink the window if the interval length exceeds k
        while sorted_ids[end] - sorted_ids[start] + 1 > k:
            current_sum -= treasure_values[sorted_ids[start]]
            start += 1
        
        # Update max_sum and best_start if this window is better
        if current_sum > max_sum or (current_sum == max_sum and sorted_ids[start] < best_start):
            max_sum = current_sum
            best_start = sorted_ids[start]
    
    return [max_sum, best_start]

# Input handling
n = int(input())  # Number of unique treasures
k = int(input())  # Length of the interval
treasures = [list(map(int, input().split())) for _ in range(n)]  # Treasure ids and values

# Solve and print the result
result = solve(n, k, treasures)
print(' '.join(map(str, result)))