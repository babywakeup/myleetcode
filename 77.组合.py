
from typing import List

class Solution:
    def __init__(self):
        self.res = []
        self.cur = []

    def dfs(self, candidates, k, idx):
        if k == 0:
            self.res.append(self.cur.copy())
            return 
        if idx == len(candidates):
            return 
        
        for i in range(idx, len(candidates)):
            self.cur.append(candidates[i])
            self.dfs(candidates, k - 1, i + 1)  # 修改这里的索引为 i + 1
            self.cur.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = list(range(1, n + 1))
        self.dfs(candidates, k, 0)
        return self.res

# 测试
sl = Solution()
n = 4
k = 2
print(sl.combine(n, k))


# 测试
sl = Solution()
n = 4
k = 2
print(sl.combine(n, k))