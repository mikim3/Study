
# 시작시간 13:34 마무리시간
from typing import List
from collections import defaultdict

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    
    # 현재 위치에 숫자가 
    
    dic = defaultdict(List)
    for i in range(len(nums)):
      dic[i] = nums[i]
    print(dic)
    for i in range(len(nums)):
      if target - nums[i] in dic:
        print(i)
    

sol = Solution()
print(sol.twoSum([2,7,11,15], 9)) # [0,1]
print(sol.twoSum([3,2,4], 6)) # [1,2]
# print(sol.canVisitAllRooms([[1],[2],[3],[]]))
