nums = list(map(int, input().split()))
output, i = 1, 0
while i < 2:
    if nums[i] % nums[2] == 0:
        output *= nums[i] // nums[2]
    elif nums[i] % nums[2] != 0:
        output *= (nums[i] // nums[2]) + 1
    i += 1
print(output)
