def solution(nums):
    nums_set = set(nums)
    nums_dict = {}
    for num in nums_set:
        nums_dict[num] = nums.count(num)
    
    n = len(nums)
    
    if len(nums_dict.keys()) >= (n // 2):
        return n // 2
    else:
        return len(nums_dict.keys())
    

def solution_1(nums):
    nums_set = set(nums)
    return min(len(nums_set), len(nums) // 2)