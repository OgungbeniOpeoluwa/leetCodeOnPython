def maxProductDiffernce(nums: list):
    first_max = max(nums)
    nums.remove(first_max)
    first_max *= max(nums)
    first_minimum = min(nums)
    nums.remove(first_minimum)
    first_minimum *= min(nums)
    return first_max - first_minimum

