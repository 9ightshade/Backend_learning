nums = [[1 , 2 ,3, 4, 5],[1, 2, 3, 4, 5],[1, 2, 300, 4, 5],[1, 20, 3, 4, 5],[-1, 2, 3, 4, 5],[1, 2, 3, 21, 18], [-1, -2, -3, -4, -5]]


"""
def find_max(nums):
    max_so_far = float("-inf")
    max = 0
    for num in nums:
        if num > max:
            max = num
    print(max)
    pass

find_max(nums)
"""

def find_max(nums):
    max_so_far = float("-inf")
    max = 0
    for num in nums:
        #print(num)
        if num > max:
            max = num
        elif num < 0:
            max = num
            
    print(max)


    pass
find_max(nums[5])

