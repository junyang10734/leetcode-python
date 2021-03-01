def find_profit(N, arr, K):
    profit = 0
    while K > 0:
        if len(arr) > 1:
            arr.sort(reverse=True)
            if arr[0] == arr[1]:
                K -= 1
                profit += arr[0]
                arr[0] -= 1
            else:
                diff = arr[0] - arr[1]
                if diff <= K:
                    K -= diff
                    profit += (arr[0] + arr[1] + 1)*diff//2
                    arr[0] = arr[1]
                else:
                    profit += (2*arr[0] - K + 1)*K // 2
                    K = 0
        else:  
            profit += (2*arr[0] - K + 1)*K // 2
            K = 0
        
    return profit



import collections
def supplierInventory(numSupplier, inventory, order):
    cnt = collections.Counter(inventory)
    curr = max(cnt)
    profit = 0

    while order > 0 and curr > 0:
        freq = cnt[curr]
        if order >= freq:
            order -= freq
            profit += curr * freq
        elif order < freq:
            profit += curr * order
            break

        curr -= 1
        cnt[curr] += freq
    
    return profit


N = 2
arr1 = [3, 4]
arr2 = [3, 4]
K = 6
print(find_profit(N, arr1, K))
print(supplierInventory(N, arr2, K))