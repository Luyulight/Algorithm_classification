def minDistance(A, B):
    # / if A[i] == B[j] => dp[i][j] = dp[i-1][j-1]
    # \ if A[i] != B[j] => dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    dp = [[0]*(len(A)+1) for _ in range(len(B)+1)]

    for i in range(1, len(A)+1):
        dp[i][0] = i

    for j in range(1, len(B)+1):
        dp[0][j] = j

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    
    return dp[-1][-1]