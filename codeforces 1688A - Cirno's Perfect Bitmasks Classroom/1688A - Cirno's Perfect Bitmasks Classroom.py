def minAnd(num):
    mask = 1
    while mask < num:
        if mask & num > 0: return mask
        mask <<= 1
    return mask

def minXOR(num):
    mask = 1
    while mask <= num:
        if mask & num == 0: return mask
        mask <<= 1
    return mask

test = int(input())
for _ in range(test):
    num = int(input())
    ans = minAnd(num)
    if ans ^ num > 0:
        print(ans)
    else:
        ans |= minXOR(num)
        print(ans)

