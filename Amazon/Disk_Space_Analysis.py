def analysis(x, space):
    occupied_space = []

    for i in range(len(space)-x+1):
        occupied_space.append(space[i:i+x])

    print(occupied_space)

    min_arr = []
    for i in range(len(occupied_space)):
        min_arr.append(min(occupied_space[i]))

    print(min_arr)

    max_ele = max(min_arr)
    return max_ele


x = 2
space = [8, 2, 4]
print(analysis(x, space))