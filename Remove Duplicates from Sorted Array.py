'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    '''
    a = 0
    while a < len(nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
        a += 1
    a = 0
    s = []
    while a < len(nums):
        if nums[a] not in s:
            s.append(nums[a])
        a += 1
    return s
    '''
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k
result = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)