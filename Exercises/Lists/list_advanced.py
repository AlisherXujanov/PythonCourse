# 1. Write a Python function to reverse a list at a specific location.
def reverse_list_at_location(arr, start, end):
    reversed = arr[start:end+1][::-1]
    return arr[:start] + reversed + arr[end+1:]

# ex
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_list_at_location(arr, 2, 5))  # [1, 2, 6, 5, 4, 3, 7, 8, 9]
# ======================================================================================
# ======================================================================================
# 2. Write a Python function find the length of the longest increasing sub-sequence in a list.
# --------------
# Original list:
# [10, 20, 30, 40, 50, 60, 70, 80]
# Length of the longest increasing sub-sequence in the said list:
# 8
# --------------
# Original list:
# [10, 20, 30, 40, 50, 30, 30, 20]
# Length of the longest increasing sub-sequence in the said list:
# 5
# --------------
# Original list:
# [-1, -2, -3, -4, -5, -11, -12, -13]
# Length of the longest increasing sub-sequence in the said list:
# 1
# --------------
# Original list:
# [10, 9, 2, 5, 3, 7, 101, 18]
# Length of the longest increasing sub-sequence in the said list:
# 4
# --------------
# ======================================================================================
# ======================================================================================
def longest_increasing_subsequence(numbers):
    """
    Find the length of the longest increasing subsequence in a given sequence of numbers.
    This function implements dynamic programming to find the length of the longest strictly
    increasing subsequence within the input list of numbers.
    Args:
        numbers (list): A list of numbers to find the longest increasing subsequence in.
    Returns:
        int: The length of the longest increasing subsequence.
    Examples:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4  # The longest increasing subsequence is [2, 5, 7, 101]
        >>> longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
        4  # The longest increasing subsequence is [0, 1, 2, 3]
        >>> longest_increasing_subsequence([])
        0  # Empty list returns 0
    Time Complexity: O(n²) where n is the length of the input list
    Space Complexity: O(n) for the dynamic programming array
    """
    if not numbers:  # Check if the list is empty
        return 0     # Return 0 for empty list
    
    # Initialize array with 1s, representing minimum subsequence length
    len_at_index = [1] * len(numbers)
    
    for current_pos in range(1, len(numbers)):        # Iterate through each position starting from index 1
        for prev_pos in range(current_pos):           # Look at all previous positions before current
            if numbers[current_pos] > numbers[prev_pos]:   # If current number is greater than previous
                len_at_index[current_pos] = max(
                        len_at_index[current_pos], 
                        len_at_index[prev_pos] + 1)  # Update length taking maximum
    
    return max(len_at_index)                          # Return the maximum length found
# ======================================================================================
# ======================================================================================


 