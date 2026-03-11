class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
          
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == target:
                    return current_sum
                
               
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum
        
