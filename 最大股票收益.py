def max_profit_dfs(present, future, budget):
    max_profit = [0]  # 用列表来存储最大收益，方便在递归中修改
    
    def dfs(index, current_budget, current_profit):
        # 递归结束条件
        if index == len(present):
            max_profit[0] = max(max_profit[0], current_profit)  # 更新最大收益
            return
        
        # 不购买当前股票
        dfs(index + 1, current_budget, current_profit)
        
        # 购买当前股票（如果预算允许）
        if present[index] <= current_budget:
            # 计算购买后的收益
            profit_after_purchase = current_profit + (future[index] - present[index])
            # 递归进入下一层
            dfs(index + 1, current_budget - present[index], profit_after_purchase)
    
    # 从第一支股票开始递归
    dfs(0, budget, 0)
    
    return max_profit[0]

# 测试样例
print(max_profit_dfs([5,4,6,2,3], [8,5,4,3,5], 10))  # 输出: 6
print(max_profit_dfs([2,2,5], [3,4,10], 6))         # 输出: 5
print(max_profit_dfs([3,3,12], [0,3,15], 10))       # 输出: 0
