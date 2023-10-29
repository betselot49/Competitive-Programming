class Solution(object):
    def maximumPopulation(self, logs):
        year_range = [0] * 101
        OFFSET = 1950
        for birth, death in logs:
            year_range[birth - OFFSET] += 1
            year_range[death - OFFSET] -= 1
            
        for idx in range(1, 101):
            year_range[idx] += year_range[idx  - 1]
            
        max_population = 0
        year = OFFSET
        
        for idx, pop in enumerate(year_range):
            if pop > max_population:
                max_population = pop
                year = idx + OFFSET
                
        return year