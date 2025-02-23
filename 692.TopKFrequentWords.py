import heapq
from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = defaultdict(int)

        # Step 1: Build frequency map
        for word in words:
            word_count[word] += 1

        # Step 2: Use min-heap of size k
        heap = []

        for word, count in word_count.items():
            # Push (count, word) into the heap
            # Negate count to sort by frequency descending
            heapq.heappush(heap, (-count, word))
            
            # Maintain heap size <= k
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract elements and reverse for correct order
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        
        return result
