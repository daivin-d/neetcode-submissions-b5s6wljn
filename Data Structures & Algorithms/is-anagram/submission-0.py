class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if s and t are equal length
        if len(s) != len(t):
            return False
        smap = {}
        tmap = {}
        for i in s:
            if i in smap:
                smap[i] +=1
            else:
                smap[i] = 1
        
        for i in t:
            if i in tmap:
                tmap[i] +=1
            else:
                tmap[i] = 1
        return  smap == tmap
        #loop through char in s and create map of s letter: frequency
        # loop through char in t and check create map  of t letter:frequency
        #check if maps are equal
        # if not return false
        # return true
        