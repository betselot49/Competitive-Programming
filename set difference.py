numEng = int(input())
engRoll = set(map(int, (input().split(" "))))
numFre = int(input())
freRoll = set(map(int, input().split(" ")))

# print(len(engRoll.difference(freRoll)))


counter = 0
for num in engRoll:
    if num not in freRoll:
        counter += 1
print(counter)
