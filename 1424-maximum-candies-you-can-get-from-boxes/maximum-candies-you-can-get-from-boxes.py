class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        hs = defaultdict(list)

        for i in range(len(containedBoxes)):
            hs[i].extend(containedBoxes[i])
        
        seen = set()
        visited = set()
        key = set()
        queue = deque(initialBoxes)
        sm = 0
        while queue:
            
            node = queue.popleft()
            visited.add(node)
            if node in seen: continue

            if node not in hs:
                # sm += candies[node]
                seen.add(node)
                continue

            for k in keys[node]:
                key.add(k)
                if k in visited and k not in seen:
                    queue.append(k)

            seen.add(node)
            # sm += candies[node]
            for n in hs[node]:
                visited.add(n)
                if status[n] == 1:
                    queue.append(n)
                else:
                    if n in key:
                        queue.append(n)
                    
        # print(seen, key)
        sm = 0
        for i in seen:
            if i in key or status[i] == 1:
                sm += candies[i]
        
        # print(sm)
        
        
        # print(off)

        return (sm )