# Insertion Sort
# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.

# nums = [2, 6, 5, 1, 3, 4]  starting point
# nums = [2, 6, 5, 1, 3, 4]  =>  2, 6   =?  i==1 no   Do nothing
# nums = [2, 6, 5, 1, 3, 4]  =>  6, 5   =?  i==1 yes  switch
# nums = [2, 5, 6, 1, 3, 4]  =>  2, 5   =?  i==0 no   Do nothing
# nums = [2, 5, 6, 1, 3, 4]  =>  6, 1   =?  i==2 yes  switch
# nums = [2, 5, 1, 6, 3, 4]  =>  2, 5   =?  i==1 yes  switch
# nums = [2, 1, 5, 6, 3, 4]  =>  2, 1   =?  i==0 yes  switch
# nums = [1, 2, 5, 6, 3, 4]  =>  5, 6   =?  i==2 no   Do nothing
# nums = [1, 2, 5, 6, 3, 4]  =>  6, 3   =?  i==3 yes  switch
# nums = [1, 2, 5, 3, 6, 4]  =>  5, 3   =?  i==2 yes  switch
# nums = [1, 2, 3, 5, 6, 4]  =>  2, 3   =?  i==1 no   Do nothing
# nums = [1, 2, 3, 5, 6, 4]  =>  6, 4   =?  i==4 yes  switch
# nums = [1, 2, 3, 5, 4, 6]  =>  5, 4   =?  i==3 yes  switch
# nums = [1, 2, 3, 4, 5, 6]  =>  4, 5   =?  i==2 yes  switch
# nums = [1, 2, 3, 4, 5, 6]  Finished

nums = [2, 6, 5, 1, 3, 4]
for i in range(1, len(nums)):
    # --------------------------------------
    key = nums[i]  # current_value
    j = i - 1  # previous_index
    # --------------------------------------
    # if PREVIOUS_IS_NOT_NEGATIVE and CURRENT_IS_SMALLER than PREVIOUS
    while j >= 0 and key < nums[j]: 
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key

print(nums)