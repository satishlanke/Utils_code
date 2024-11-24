from itertools import combinations
from bisect import bisect_left

def solve(n, spices, target):
    # Helper function to generate all subset sums
    def get_subset_sums(arr):
        subset_sums = []
        for i in range(len(arr) + 1):
            for subset in combinations(arr, i):
                subset_sums.append(sum(subset))
        return subset_sums
    
    # Split spices into two halves
    left, right = spices[:n // 2], spices[n // 2:]
    
    # Generate subset sums for each half
    left_sums = get_subset_sums(left)
    right_sums = get_subset_sums(right)
    
    # Sort right_sums for binary search
    right_sums.sort()
    
    # Find the closest sum to the target
    closest_sum = float('inf')
    closest_diff = float('inf')
    
    for sum_left in left_sums:
        # Complement needed from right_sums
        complement = target - sum_left
        
        # Binary search for the closest complement in right_sums
        idx = bisect_left(right_sums, complement)
        
        # Check the current and previous elements (if any) for closest match
        for i in [idx - 1, idx]:
            if 0 <= i < len(right_sums):
                total_sum = sum_left + right_sums[i]
                diff = abs(total_sum - target)
                
                # Update closest if:
                # 1. Difference is smaller
                # 2. Difference is the same but the sum is smaller numerically
                if diff < closest_diff or (diff == closest_diff and total_sum < closest_sum):
                    closest_diff = diff
                    closest_sum = total_sum
    
    return closest_sum

# Input handling
n = int(input())  # Number of spices
spices = list(map(int, input().split()))  # List of spice strengths
target = int(input())  # Target flavor

# Solve and print the result
out = solve(n, spices, target)
print(out)