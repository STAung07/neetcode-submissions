class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count occurence of each num
        nums.sort()
        min_heap = []
        curr = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] != curr:
                min_heap.append((count, curr))
                count = 1
            else:
                count += 1
            curr = nums[i]
        min_heap.append((count, curr))
        
        min_heap.sort(key=lambda x: x[0])

        # slice by k
        sliced_list = min_heap[len(min_heap)-k:]
        return [item[1] for item in sliced_list]
