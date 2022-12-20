class Solution:
    def similarPairs(self, words: List[str]) -> int:
        list1 = []
        for word in words:
            Set = set(word)
            join = ''.join(Set)
            sort = sorted(join)
            sort = ''.join(sort)
            list1.append(sort)
            
        i = 0
        counter = 0
        while i < len(list1):
            j = i + 1
            while j < len(list1):
                if list1[i] == list1[j]:
                    counter += 1
                j += 1
            i += 1
        return counter