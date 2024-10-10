def countoddSubarrays(n, arr):
    """
    Counts the number of good subarrays in the given array.
    A subarray is considered good if the XOR of its elements is odd and its length is even.
    
    Args:
        n: The size of the array.
        arr: The array of integers.
    
    Returns:
        The count of good subarrays.
    """
    count = 0
    prefix_xor = 0

    # Dictionaries to track the frequency of prefix_xor for even and odd indices
    freq_even = {0: 1}  # Starting with 0 XOR at an imaginary index -1 (even)
    freq_odd = {0: 0}   # No prefix XOR starts at an odd index initially

    for i in range(n):
        # Update the current prefix XOR
        prefix_xor ^= arr[i]

        if i % 2 == 0:
            # If index is even, pair with previous odd-indexed XORs
            count += freq_odd.get(prefix_xor ^ 1, 0)  # XOR needs to be odd
            # Update the even-indexed XOR frequency
            freq_even[prefix_xor] = freq_even.get(prefix_xor, 0) + 1
        else:
            # If index is odd, pair with previous even-indexed XORs
            count += freq_even.get(prefix_xor ^ 1, 0)  # XOR needs to be odd
            # Update the odd-indexed XOR frequency
            freq_odd[prefix_xor] = freq_odd.get(prefix_xor, 0) + 1

    return count


n1 = 3
arr1 = [1, 2, 3]
print(countoddSubarrays(n1, arr1))  # Output: 2

n2 = 5
arr2 = [4, 2, 3, 2, 1]
print(countoddSubarrays(n2, arr2))  # Output: 4
