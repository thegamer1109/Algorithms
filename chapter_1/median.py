def median_followers(nums):
    med = 0
    Nlist = sorted(nums)
    n = len(nums)
    if n == 0:
        return None
    if n % 2 == 0:
        med = (Nlist[n//2] + Nlist[(n//2)-1]) / 2
    else:
        med = Nlist[n // 2]
        
    return med

if __name__ == '__main__':
    nums = [12,12,12]
    print(median_followers(nums))