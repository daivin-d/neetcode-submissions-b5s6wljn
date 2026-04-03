class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
        # hash approach
        # declare set {}
        #loop through array check if nums[i] in {}
        # if so return true, breaking loop
        # else add to {} and repeat
        # once loop ends return false
