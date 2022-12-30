testCase = int(input())

for i in range(testCase):
    momentLight = input().split(" ")[1]
    lights = input()
    
    lights += lights
    
    if momentLight == "g":
        print(0)
    else:
        minSecond = 0
        curSecond = 0
        increment = 0
        green = 0
        for light in lights[::-1]:
            if light == "g":
                minSecond = max(minSecond, curSecond)
                curSecond = 0
                increment = 0
            else:
                increment += 1
                if light == momentLight:
                    curSecond = increment
        
        print(minSecond)
