numEng  = input()
engRoll = set(map(int, input().split(" ")))
numFre = input()
freRoll = set(map(int, input().split(" ")))

print(len(engRoll.union(freRoll)))
