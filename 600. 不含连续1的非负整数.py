def findIntegers(n):
    bin_n = bin(n)[2:]
    m = len(bin_n)
    # 求k位二进制数字不含连续1的数字的个数
    ##定义 dp[0][k], dp[1][k] 表示首位为0或1的k位二进制数字中不含连续1的个数
    dp = [[0]*(m+1) for _ in range(2)]
    dp[0][1], dp[1][1]=1,1
    for j in range(2,m+1):
        dp[0][j]=dp[0][j-1]+dp[1][j-1]
        dp[1][j]=dp[0][j-1]
    DP=[dp[0][i]+dp[1][i] for i in range(m+1)]
    DP[0]=1
    # 从高位到低位来看
    res = 0
    for k in range(m):
        #从高位到低位遍历二进制串，检查每一位，
        #如果当前位为 1，并且在前面的子串中不包含连续的 11，则累加该位置的贡献值。
        if bin_n[k]=='1' and '11' not in bin_n[0:k]: 
            res+=DP[m-k-1] 
    # 加上n本身
    if '11' not in bin_n: res+=1 
    return res

    

n=6

print(findIntegers(n))
