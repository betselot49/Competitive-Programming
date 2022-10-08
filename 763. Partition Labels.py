class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partition = [[s[0]]]
        counter, j = [1], 1
      
        while j < len(s):
            i = 0
            while i < len(partition) and s[j] not in partition[i]:
                i += 1
            if i == len(partition):
                partition.append([s[j]])
                counter.append(1)
            else:
                while len(partition) > i+1:
                    partition[i] += partition.pop()
                    counter[i] += counter.pop()
                partition[i] += [s[j]]
                counter[i] += 1
            j += 1
        return counter
