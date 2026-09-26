
#reverse string

class Solution(object):
    import math
    def reverseString(self, s):
        start=0
        end=len(s)-1
        while end>start:
            temp=s[start]
            s[start]=s[end]
            s[end]=temp
            start+=1
            end-=1
        return(s)

#two sum
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            if target-nums[i] in nums:
                res=[i,nums.index(target-nums[i])]
                if res[0]!=res[1]:
                   return res


#isPalindrome

class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        res=0
        x1=x
        while x1>0:
            res=res*10 + x1%10
            x1//=10
        return(res==x)