# Function to solve the knapsack problem using backtracking
def knapsack_backtracking(weights, values, capacity, n):
    # Base case: If no items are left or the capacity is 0, return 0 value
    if n == 0 or capacity == 0:
        return 0

    # If the weight of the nth item is more than the capacity, it cannot be included
    if weights[n-1] > capacity:
        return knapsack_backtracking(weights, values, capacity, n-1)
    
    # Case 1: nth item is included
    include = values[n-1] + knapsack_backtracking(weights, values, capacity - weights[n-1], n-1)
    
    # Case 2: nth item is not included
    exclude = knapsack_backtracking(weights, values, capacity, n-1)
    
    # Return the maximum of including or excluding the nth item
    return max(include, exclude)

# Example usage
weights = [10, 20, 30]  # Weights of the items
values = [60, 100, 120] # Values of the items
capacity = 50           # Maximum capacity of the knapsack
n = len(weights)        # Number of items

# Solve the knapsack problem
max_value = knapsack_backtracking(weights, values, capacity, n)
print(f"The maximum value that can be obtained is {max_value}")
