from typing import List
class Solution:
    def __init__(self):
        self.res=[]
        self.combine=[]
    def dfs(self, candidates, target, idx):
        if target==0:
            self.res.append(self.combine.copy())
            return
        if idx==len(candidates):
            return
        cnt=1
        while(idx+1<len(candidates) and candidates[idx]==candidates[idx+1]):
            idx+=1
            cnt+=1
        for i in range(cnt+1):
            if target-i*candidates[idx]<0:
                break
            self.dfs(candidates, target-i*candidates[idx],idx+1)
            self.combine.append(candidates[idx])

        for i in range(cnt+1):
            if target-i*candidates[idx]<0:
                break
            self.combine.pop()
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates,target,0)
        return self.res
  
sl=Solution()
candidates=[1,1,2]
target=2
print(sl.combinationSum2(candidates,target))