# Two Pointers Algorithm

## Overview 📚
Two Pointers is a technique where two pointers iterate through a data structure in a coordinated way. This pattern is particularly efficient for solving problems with sequences (arrays, strings, linked lists) while maintaining space complexity of O(1).

## Why Use Two Pointers? 🤔
- Reduces time complexity from O(n²) to O(n) in many cases
- Helps avoid nested loops
- Maintains minimal space complexity
- Efficient for sorted array operations

## Common Use Cases 🎯
1. Meeting pointers (start/end moving toward each other)
2. Fast/slow pointers (detecting cycles)
3. Parallel pointers (same direction at different speeds)

## Effective Situations 🚀
- Searching pairs in sorted arrays
- Palindrome validation
- Cycle detection in linked lists
- Sliding window problems
- Array partition problems

## Examples 

### Beginner Level 🌱 
```python
# Find if array has a pair that sums to target
# NOTE: Here the array is sorted
def findPair(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return True
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return False
```

### Intermediate Level 🔨 
```python
# Remove duplicates from sorted array in-place
# NOTE: This function returns the length of the new array
def removeDuplicates(arr):
    if not arr:
        return 0
    slow = 0
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

### Advanced Level 🚀

```python
# Find the longest substring without repeating characters
def lengthOfLongestSubstring(s):
    seen = {}
    start = max_length = 0
    
    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        seen[char] = end
    
    return max_length
```

## Time Complexity
Most Two Pointers solutions achieve O(n) time complexity, making them significantly more efficient than brute force approaches that often require O(n²).

## Space Complexity
Generally O(1) as only two pointers are used regardless of input size.

## Tips
- Always consider if input needs to be sorted
- Watch for edge cases (empty arrays, single elements)
- Be careful with pointer movement conditions
- Consider using while loops for more control