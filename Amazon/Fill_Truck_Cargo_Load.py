def loadTheCargo(num, containers, itemSize, itemsPerContainer, cargoSize):
    arr = []
    for i in range(num):
        arr += [itemsPerContainer[i]] * containers[i]
    arr.sort(reverse=True)
    return sum(arr[:cargoSize])



if __name__ == '__main__':
    num = 3
    containers = [3, 1, 2]
    itemSize = 3
    itemPreContainer = [1, 2, 3]
    cargoSize = 4
    print(loadTheCargo(num, containers, itemSize, itemPreContainer, cargoSize))