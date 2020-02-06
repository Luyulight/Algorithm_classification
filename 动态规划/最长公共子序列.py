def findLength(A, B):
    # / dp[i][j] = dp[i-1][j-1] + 1 if A[i] == B[j]
    # \ dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if A[i] != B[j] 非连续
    dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]
    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    return max(max(row) for row in dp)