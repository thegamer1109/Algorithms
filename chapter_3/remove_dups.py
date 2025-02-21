def remove_duplicates(nums):
    seen = set()
    unique_nums = []
    for i in nums:
        if i not in seen:
            seen.add(i)
            unique_nums.append(i)
    return unique_nums