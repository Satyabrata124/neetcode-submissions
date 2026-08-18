class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        pre =[0] * n
        post=[0] * n
        ret=[0] * n

        pre[0]=post[n-1]=1
        for i in range(1,len(nums)):
            pre[i]=nums[i-1] * pre[i-1]
        for i in range(n-2,-1,-1):
            post[i]=nums[i+1] * post[i+1]
        for i in range(n):
            ret[i]=pre[i]*post[i]

        return ret
        