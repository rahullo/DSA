def generate_binary_strings(n, prefix=""):
    # Base case: If the length of the prefix equals n, print the prefix
    if n == 0:
        print(prefix)
    else:
        # Recursively add '0' and '1' to the prefix and reduce the length by 1
        generate_binary_strings(n - 1, prefix + "1")
        generate_binary_strings(n - 1, prefix + "0")

# Example usage:
n = 3  # Length of the binary strings
generate_binary_strings(n)
