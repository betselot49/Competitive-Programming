class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def compute(state, change):
            state[change[0]] += change[1]
            if state[change[0]] == -1:
                state[change[0]] = 9
            if state[change[0]] == 10:
                state[change[0]] = 0
            return state
        
        def unloack(target):
            NEXT_STATE = [(0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2 ,-1), (3, 1), (3, -1)]
            queue = deque([([0, 0, 0, 0], 0)])
            deadend = set(deadends)
            
            while queue:
                current, level = queue.popleft()
                curr_string = "".join(map(str, current))
                if curr_string in deadend: continue
                if curr_string == target: return level
                deadend.add(curr_string)
                for value in NEXT_STATE:
                    computed = compute(current[:], value)
                    queue.append((computed, level+1))
                            
            return -1
        
        return unloack(target)