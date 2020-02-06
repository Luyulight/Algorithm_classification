def search(nums, t):
    # 先找到最小值的index
    # 确定要找的数是否在list中
    # 确定要找的数在前半段还是后半段
    # 二分查找idx

    if not nums:
        return -1

    # 先找到最小值的index
    min_idx = 0
    if nums[0] < nums[-1]:
        pass
    else:
        l = 0
        r = len(nums)-1
        while l < r:
            m = (l+r) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
        
        min_idx = l

    max_idx = 0
    if min_idx == 0:
        max_idx = len(nums)-1
    else:
        max_idx = min_idx - 1

    # 确定要找的数是否在list中
    if t < nums[min_idx] or t > nums[max_idx]:
        return -1
    
    # 确定要找的数在前半段还是后半段
    if t < nums[0]:
        l = min_idx
        r = len(nums) - 1
    else:
        l = 0
        r = max_idx

    # 二分查找idx
    while l < r:
        m = (l+r) // 2
        if nums[m] < t:
            l = m+1
        else:
            r = m
        
    return l