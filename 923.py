# 923. 3Sum With Multiplicity
# Two Pointers

# https://leetcode.com/problems/3sum-with-multiplicity/solution/

# three pointers
# runtime: faster than 13.54%
class Solution1:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        arr.sort()
        for i,a in enumerate(arr):
            t = target - a
            j, k = i+1, len(arr)-1
            while j < k:
                if arr[j] + arr[k] < t:
                    j += 1
                elif arr[j] + arr[k] > t:
                    k -= 1
                else:
                    if arr[j] != arr[k]:
                        left = right = 1
                        while j + 1 < k and arr[j+1] == arr[j]:
                            left += 1
                            j += 1
                        while k - 1 > j and arr[k-1] == arr[k]:
                            right += 1
                            k -= 1
                        res += left * right
                        j += 1
                        k -= 1
                    else:
                        res += (k-j+1)*(k-j)//2
                        break
                        
        return res % (10**9 + 7)


# counter + three pointers
# runtime: faster than 71.05%
class Solution2:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        res = 0
        arr.sort()
        count = Counter(arr)
        keys = sorted(set(arr))
        
        for i,a in enumerate(keys):
            t = target - a
            j, k = i, len(keys)-1
            while j <= k:
                b, c = keys[j], keys[k]
                if b + c < t:
                    j += 1
                elif b + c > t:
                    k -= 1
                else:
                    if i < j < k:
                        res += (count[a] * count[b] * count[c])
                    elif i == j < k:
                        res += (count[a] * (count[a]-1) * count[c])//2
                    elif i < j == k:
                        res += (count[a] * (count[b]-1) * count[b])//2
                    else:
                        res += (count[a]*(count[a]-1)*(count[a]-2)) // 6

                    j += 1
                    k -= 1

                        
        return res % (10**9 + 7)