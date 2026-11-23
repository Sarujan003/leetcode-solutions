# Q1

def ZeroOneKnapsack(val, wt, capacity):
    vw = [(v,w) for v,w in zip(val, wt)]

    vw = sorted(vw, key=lambda x:x[1])

    dp = [[0] * (capacity + 1) for i in range(len(val) + 1)]

    for i in range(1, len(val)+1):
        v, w = vw[i-1]
        for j in range(1, capacity+1):

            if j < w:
                dp[i][j] = dp[i-1][j]

            else:
                dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])


    return vw, dp


w = 6
val = [1, 2, 3]
wt = [4, 5, 1]

print(ZeroOneKnapsack(val, wt, w))