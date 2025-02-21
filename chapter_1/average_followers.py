def avg_followers(nums):
    total = 0
    if len(nums) == 0:
        return None
    for i in nums:
        total += i
    return total / len(nums)