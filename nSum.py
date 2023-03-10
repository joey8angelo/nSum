class NSum:
    def nSum(self, nums, target, n):
        nums.sort()
        ans = []
        self._nSum(nums, target, n, 0, ans, [])
        return ans
    
    def _nSum(self, nums, target, n, p, ans, prev):
        i = p
        while i < len(nums)-(n-1):
            if n == 3:
                self.twoSum(nums, i+1, target-nums[i], ans, prev+[nums[i]])
            else:
                self._nSum(nums, target-nums[i], n-1, i+1, ans, prev+[nums[i]])
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1
        return ans
    
    def twoSum(self, nums, p, target, ans, prev):
        l = p
        r = len(nums)-1
        
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                ans.append(prev+[nums[l], nums[r]])
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif s < target:
                l += 1
            else:
                r -= 1