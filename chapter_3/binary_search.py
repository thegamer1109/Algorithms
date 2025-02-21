'''
Pseudocode
Given two inputs:

An array of n elements sorted from least to greatest
A target value:
Do the following:

Set low = 0 and high = n - 1.
While low <= high:
Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
If array[median] == target, return True
Else if array[median] < target, set low to median + 1
Otherwise set high to median - 1
Return False
At each iteration of loop, we halve the list. Which makes the algorithm O(log(n)). In other words, to add one more step to the runtime, we'd have to double the size of the input. Binary searches are fast.
'''

'''
Assignment
We have a popular influencer using our LockedIn app, and she needs to be able to quickly search for posts from a particular day. This function will be the backbone of her search screen.

Complete the binary_search function. It should follow the algorithm as described above.
'''

def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
            
