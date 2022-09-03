def countingValleys(steps, path):
    i, U, D, V = 0, 0, 0, 0
    while i < steps:
        if path[i] == "U":
            U += 1
        else:
            D += 1
            V += 1
        i += 1
        while U != D:
            if path[i] == "U":
                U += 1
            else:
                D += 1
            i += 1
    return V
