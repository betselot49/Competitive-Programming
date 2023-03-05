class Solution:
    def predict(self, array, left, right, turn):
        if right - left == 0:
            score = [0, 0]
            score[turn] += array[left]
            return score
        elif right - left == 1:
            score = [0, 0]
            score[turn] += max(array[left], array[right])
            score[1-turn] += min(array[left], array[right])
            return score
        
        first_choice = self.predict(array, left+1, right, 1-turn)
        first_choice[turn] += array[left]
        
        second_choice = self.predict(array, left, right-1, 1-turn)
        second_choice[turn] += array[right]
        
        return first_choice if first_choice[turn] >= second_choice[turn] else second_choice 
        
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        result = self.predict(nums, 0, len(nums)-1, 0)
        return result[0] >= result[1]
