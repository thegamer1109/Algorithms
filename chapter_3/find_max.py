def find_max(nums):
    max = -1
    
    if nums == []:
        return None
    
    else:
        for i in nums:
            if i > max:
                max = i
    
    return max


if __name__ == '__main__':
    nums = []
    print(find_max(nums))
    nums = [1]
    print(find_max(nums))