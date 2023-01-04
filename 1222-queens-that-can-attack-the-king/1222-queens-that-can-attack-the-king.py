class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:      
        setQueens = {(point1, point2) for point1, point2 in queens}
        attackers = []
        case = [-1, 0, 1]
        
        for index1 in case:
            for index2 in case:
                for index3 in range(8):
                    point1, point2 = king[0] + index1 * index3, king[1] + index2 * index3
                    if (point1, point2) in setQueens:
                        attackers.append([point1, point2])
                        break
                        
        return attackers
    
    

    
    
    
#  < ==========  bruteforce   ============ > 
    
#         possibleQueens = [0] * 8
        
#         for queen in queens:
#             difference = [0, 0]
#             difference[0] = queen[0] - king[0]
#             difference[1] = queen[1] - king[1]
            
#             if difference[0] == 0 and difference[1] > 0:
#                 if possibleQueens[0] == 0:
#                     possibleQueens[0] = queen    
#                 else:
#                     possibleQueens[0] = self.minDistance(king, queen, possibleQueens[0])
#             elif difference[0] == 0 and difference[1] < 0:
#                 if possibleQueens[1] == 0:
#                     possibleQueens[1] = queen
#                 else:
#                     possibleQueens[1] = self.minDistance(king, queen, possibleQueens[1])
#             elif difference[0] > 0 and difference[1] == 0:
#                 if possibleQueens[2] == 0:
#                     possibleQueens[2] = queen
#                 else:
#                     possibleQueens[2] = self.minDistance(king, queen, possibleQueens[2])
#             elif difference[0] < 0 and difference[1] == 0:
#                 if possibleQueens[3] == 0:
#                     possibleQueens[3] = queen
#                 else:
#                     possibleQueens[3] = self.minDistance(king, queen, possibleQueens[3])
#             elif difference[0] > 0 and difference[0] == difference[1]:
#                 if possibleQueens[4] == 0:
#                     possibleQueens[4] = queen
#                 else:
#                     possibleQueens[4] = self.minDistance(king, queen, possibleQueens[4])
#             elif difference[0] < 0 and difference[0] == difference[1]:
#                 if possibleQueens[5] == 0:
#                     possibleQueens[5] = queen
#                 else:
#                     possibleQueens[5] = self.minDistance(king, queen, possibleQueens[5])
#             elif difference[0] > 0 and difference[1] < 0 and -difference[0] == difference[1]:
#                 if possibleQueens[6] == 0:
#                     possibleQueens[6] = queen
#                 else:
#                     possibleQueens[6] = self.minDistance(king, queen, possibleQueens[6])
#             elif difference[0] < 0 and difference[1] > 0 and -difference[0] == difference[1]:
#                 if possibleQueens[7] == 0:
#                     possibleQueens[7] = queen
#                 else:
#                     possibleQueens[7] = self.minDistance(king, queen, possibleQueens[7])
           
#         queensAtack = []
#         for queen in possibleQueens:
#             if queen:
#                 queensAtack.append(queen)
            
#         return queensAtack

#         def minDistance(self, reference, point1, point2):
#             distance1 = ((reference[0] - point1[0]) ** 2 + (reference[1] - point1[1]) ** 2) ** 0.5
#             distance2 = ((reference[0] - point2[0]) ** 2 + (reference[1] - point2[1]) ** 2) ** 0.5
#             if distance1 < distance2:
#               return point1
#             return point2



    
    
        