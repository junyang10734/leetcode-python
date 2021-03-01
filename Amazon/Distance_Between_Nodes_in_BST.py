class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDistance(root, p, q):
    if not root or p == q:
        return 0

    leftD = findDistance(root.left, p, q)
    rightD = findDistance(root.right, p, q)

    if leftD > 0 and rightD > 0:
        return leftD + rightD
    elif leftD > 0 and (root == p or root == q):
        return leftD
    elif rightD > 0 and (root == p or root == q):
        return rightD
    elif leftD == 0 and rightD == 0:
        return 0 if (root != p or root != q) else 1
    else:
        return max(leftD, rightD) + 1


def distance_in_bst(root, p, q):
    def depth(root, node, d=0):
        if not root:
            return 
        if node.val == root.val:
            return d
        return depth(root.left, node, d+1) or depth(root.right, node, d+1)

    def lca(root, p, q):
        if root.val < p.val:
            return lca(root.right, p, q)
        elif root.val > q.val:
            return lca(root.left, p, q)
        else:
            return root

    return depth(root, p) + depth(root, q) - 2 * depth(root, lca(root, p, q).val)




class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(tree, val):
    if not tree:
        tree = Node(val)
    elif val < tree.val:
        tree.left = insert(tree.left, val)
    else:
        tree.right = insert(tree.right, val)
    return tree

def find(tree, val):
    path = []
    while tree:
        path.append(tree.val)
        if val == tree.val:
            return path
        elif val < tree.val:
            tree = tree.left
        else:
            tree = tree.right
    return None


def bstDistance(nums, node1, node2) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    tree = None
    for n in nums:
        tree = insert(tree, n)
    left = find(tree, node1)
    right = find(tree, node2)
    if not left or not right:
        return -1
    return len(set(left).symmetric_difference(right))
    
    
    
if __name__ == "__main__":
    nums = [2, 1, 3]
    node1 = 1
    node2 = 3
    print(bstDistance(nums, node1, node2))