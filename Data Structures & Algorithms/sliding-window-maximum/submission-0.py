class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        if k >= len(nums):
            return [max(nums)]

        entry_dict = defaultdict(int)
        heap = []
        res = []

        for i in range(k):
            entry_dict[nums[i]] += 1
            heapq.heappush_max(heap,nums[i])
        
        res.append(heap[0])
        for i in range(k,len(nums)):
            heapq.heappush_max(heap,nums[i])
            entry_dict[nums[i]] += 1

            entry_dict[nums[i-k]] -= 1
            while entry_dict[heap[0]] == 0:
                heapq.heappop_max(heap)
                
            
            res.append(heap[0])
        return res

        