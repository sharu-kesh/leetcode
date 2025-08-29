class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mpp = defaultdict(int)
        res = []

        for i in nums:
            mpp[i] += 1
            
            if len(mpp) > 2:
                new = defaultdict(int)
                for key, val in mpp.items():
                    if val > 1:
                        new[key] = val - 1
                mpp = new
        
        for key in mpp:
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        return res
        