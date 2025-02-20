def find_minimum(nums):
    minimum = float('inf')
    if len(nums) == 0:
        return None
    for number in nums:
        if number < minimum:
            minimum = number
    return minimum