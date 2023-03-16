
# this code is incomplete

visted = [0,0,0,0] # up to the number of nodes

for a in nodes:
    dfs(a)

def dfs(node):
    visted[0] = 1

    for a in node.children:
        dfs(a)