import collections

def dfs(root):
    if root is None:
        return []
    result = []

    q = collections.deque([root])
    while len(q) != 0:
        numnodes = len(q)
        temp = []
        for _ in range(numnodes):
            node = q.popleft()
            if node.left is not None: # if n-nary tree tjhen use "for child in node,children: q. append(child)""
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            temp.append(node.val)
        result.append(temp)
    return result

