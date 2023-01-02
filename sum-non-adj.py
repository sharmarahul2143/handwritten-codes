def largest_sum_nonadjacent(nums):
  if not nums:
    return 0

  if len(nums) == 1:
    return nums[0]

  return max(largest_sum_nonadjacent(nums[1:]), nums[0] + largest_sum_nonadjacent(nums[2:]))
print(largest_sum_nonadjacent([2, 4, 6, 2, 5]))  # should print 13
print(largest_sum_nonadjacent([5, 1, 1, 5]))  # should print 10
