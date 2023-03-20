class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        N = len(s)
        
        excess = defaultdict(int)
        length = 0
        for char in count:
            if count[char] > N//4:
                excess[char] = count[char] - (N // 4)
                length += count[char] - (N // 4)
        if length == 0: return 0  # length == 0 means it is balanced or no excess!!!
        
        left = curr_len = 0
        min_length = float("inf")
        window = defaultdict(int)
        for right, char in enumerate(s):
            if char in excess:
                window[char] += 1
                curr_len += 1 if window[char] <= excess[char] else 0
                    
            while curr_len == length:
                min_length = min(min_length, right- left + 1)
                if s[left] in excess:
                    window[s[left]] -= 1
                    if window[s[left]] < excess[s[left]]:
                        curr_len -= 1
                        
                left += 1
        return 0 if min_length == float("inf") else min_length