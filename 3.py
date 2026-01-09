class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeats =set()
        l ,r =  0 ,0 
        res = 0 

        while l <= r and r <len(s) :
            if s[r] not in repeats:
                res =max(res , r-l+1)
                repeats.add(s[r])
                r+=1 
            else:
                repeats.remove(s[l])
                l+=1 
        return res







       
           

