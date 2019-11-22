"""
* window sum就是给一个包含整数的arraylist和一个window size k，
* 返回所有长度为k的窗口的数的和。
* 比如数组[1,2,3,4,5],window size 2，
* 那么长度为2的窗口就是[1,2],[2,3],[3,4],[4,5],和就依次是3,5,7,9.
"""


def window_sum(array_list, k):
    result = []
    if not list or len(array_list) == 0:
        return res
    if not k or k > len(array_list):
        return None

    for i in range(len(array_list)-k+1):
        win_sum = list[i]
        j = 1
        while j < k:
            win_sum += array_list[i+j]
            j += 1
        result.append(win_sum)
    return result


if __name__ == "__main__":
    array_list = [1, 2, 3, 4, 5]
    k = 3
    res = window_sum(array_list, k)
    print(res)
