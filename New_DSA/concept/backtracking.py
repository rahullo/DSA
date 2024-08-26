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
# generate_binary_strings(n)


def generate_k_ary_strings(n, k, prefix=""):
    # Base case: If the length of the prefix equals n, print the prefix
    if n == 0:
        print(prefix)
    else:
        # Recursively add digits from 0 to k-1 to the prefix and reduce the length by 1
        for i in range(k):
            generate_k_ary_strings(n - 1, k, prefix + str(i))

# Example usage:
n = 3  # Length of the strings
k = 3  # Base (for ternary strings, k=3)
generate_k_ary_strings(n, k)
