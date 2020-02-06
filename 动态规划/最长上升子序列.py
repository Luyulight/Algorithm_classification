def lengthOfLIS(nums):
    # dp[i] = dp[j] + 1 if nums[j] < nums[i]
    n = len(nums)
    if n == 0:
        return 0
    
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)