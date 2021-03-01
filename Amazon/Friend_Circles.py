def friend_circles(relationships):
    visited = set()
    res = 0
    def dfs(node):
        for neighbor, connected in enumerate(relationships[node]):
            if connected and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    
    for i in range(len(relationships)):
        if i not in visited:
            dfs(i)
            res += 1
    return res


if __name__ == '__main__':
    relationships = [[1, 1, 0],
                     [1, 1, 0],
                     [0, 0, 1]]
    res = friend_circles(relationships)
    print(res)