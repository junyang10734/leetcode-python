def unequalTriplets(nums) -> int:
    res = 0
    i, j = 0, 0
    while i < len(nums)-2 and j < len(nums)-1:
        while nums[i] == nums[j] and j < len(nums)-1:
            j += 1

        if j > len(nums)-2:
            i += 1
            j = i + 1
            continue
        
        k = j + 1
        while k < len(nums):
            if nums[k] != nums[j] and nums[k] != nums[i]:
                res += 1
                print('i:' + str(nums[i]) + '    j:' +
                      str(nums[j]) + '    k:' + str(nums[k]))
            k += 1

        if j == len(nums)-2:
            i += 1
            j = i + 1
        else:
            j += 1

    return res

arr = [4,4,2,4,3]
unequalTriplets(arr)