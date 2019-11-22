# leetcode 48: rotate image

def rotate(matrix, flag):
    """
    Do not return anything, modify matrix in-place instead.
    flag == 1: 右转
    flag == 0: 左转
    """

    if matrix:
        rows, cols = len(matrix), len(matrix[0])
        if flag == 1:
            for i in range(int(rows / 2)):
                for j in range(cols):
                    matrix[i][j], matrix[rows-i-1][j] = matrix[rows-i-1][j], matrix[i][j]
        else:
            for i in range(rows):
                for j in range(int(cols/2)):
                    matrix[i][j], matrix[i][cols-j-1] = matrix[i][cols-j-1], matrix[i][j]

        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


if __name__ == "__main__":
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    flag = 0
    res = rotate(matrix, flag)
    print(res)
