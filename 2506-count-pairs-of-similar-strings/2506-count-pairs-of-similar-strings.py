class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def fact(num):
            for j in range(num-1, 1, -1):
                num *= j
            return num
        list1 = []
        for word in words:
            Set = set(word)
            join = ''.join(Set)
            sort = sorted(join)
            sort = ''.join(sort)
            list1.append(sort)
            
#         print(list1)
#         i = 0
#         counter = 0
#         while i < len(list1):
#             j = i + 1
#             while j < len(list1):
#                 if list1[i] == list1[j]:
#                     counter += 1
#                 j += 1
#             i += 1
#         return counter
        c = 0
        list1 = dict(Counter(list1))
        for word in list1:
            num = list1[word]
            if num > 2:    
                c += fact(num)/(fact(num-2)*2)  
            elif num == 2:
                c += 1
        return int(c)