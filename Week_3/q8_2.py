def count_above_average(nums):
    avg = sum(nums) / len(nums)
    return sum(1 for n in nums if n > avg)

# return sum(1 for n in nums if n > avg) -> isme [1,1,1,1,1] aise list ban jayegi jaha jaha avg se bada hoga n and last mei sum means summation of the list giving us the final answer for the question.