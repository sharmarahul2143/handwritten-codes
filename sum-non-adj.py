def largest_sum_non_adjacent(nums):
    if not nums:
        return 0

    # initialize the maximum sum to be the first number in the list
    max_sum = nums[0]

    # initialize the second maximum sum to be 0
    second_max_sum = 0

    # iterate through the rest of the list
    for i in range(1, len(nums)):
        # update the second maximum sum to be the maximum of the current second maximum sum and the previous maximum sum
        second_max_sum = max(second_max_sum, max_sum)

        # update the maximum sum to be the maximum of the current maximum sum and the previous second maximum sum plus the current number
        max_sum = max(max_sum, second_max_sum + nums[i])

    # return the maximum sum
    return max_sum