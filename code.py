----using set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=set()
        for index,num in enumerate(nums):
            comple=target - num
            if comple in s:
                return [index, nums.index(comple)]
            s.add(num)

  --using sort and two array
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     left=0
    #     right=len(nums)-1
    #     temp = sorted(enumerate(nums), key=lambda x: x[1])

    #     result=[]
    #     while left<right:
    #         if temp[left][1] + temp[right] [1]< target:
    #             left+=1
    #         elif temp[left][1]+ temp[right][1] <target:
    #             right-=1 
    #         elif temp[left][1]+ temp[right][1] ==target:
    #             return (temp[left][0],temp[right][0])

        def twoSum(self, nums: List[int], target: int) -> List[int]:
            sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
            left, right = 0, len(nums) - 1
            while left < right:
                current_sum = sorted_nums[left][1] + sorted_nums[right][1]
                if current_sum == target:
                    return [sorted_nums[left][0], sorted_nums[right][0]]
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

            return []


                


        
