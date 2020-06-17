class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
            
        # print(f)
        
        heap = [(0, src, k + 1)]
        
        # print(heap)
        
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
            # print(heap)
        return -1
        