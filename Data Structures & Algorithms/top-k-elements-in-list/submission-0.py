class Solution:
    def topKFrequent(self, nums: List[int], L: int) -> List[int]:
        k={}
        s=[]
        for i in nums:
            if i not in k:
                k[i]=1
            else:
                k[i]+=1
        a = []
        for num in k.keys():
            heapq.heappush(a, (k[num], num))
            if len(a) > L:
                heapq.heappop(a)

        res = []
        for i in range(L):
            res.append(heapq.heappop(a)[1])
        return res