class Solution:
    def numTeams(self, rating: List[int]) -> int:
        greater_than_me = {}
        less_tham_me = {}
        for i in range(len(rating)):
            greater_count = less_count = 0
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    greater_count += 1
                elif rating[i] > rating[j]:
                    less_count += 1
                    
            greater_than_me[i] = greater_count
            less_tham_me[i] = less_count
            
        # Counting
        number_of_teams = 0
        for i in range(len(rating)):
            for j in range(i + 1, len(rating)):
                if rating[i] < rating[j]:
                    number_of_teams += greater_than_me[j]
                else:
                    number_of_teams += less_tham_me[j]
                    
        return number_of_teams
                    
                

        
        