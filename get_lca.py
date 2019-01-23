class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Making Node As per mentioned tree diagram
rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(4)
rootNode.left.right = Node(5)
rootNode.right.left = Node(6)
rootNode.right.right = Node(7)
rootNode.left.left.left = Node(8)
rootNode.left.left.right = Node(9)


# Main lca function
def lca(root=rootNode, node1=1, node2=2):
    # To store paths to node1 and node2 from the root
    path1 = []
    path2 = []

    # Find paths from root to node1 and root to node2.
    # If either node1 or node2 is not present , return -1
    if (not findnode(root, path1, node1) or not findnode(root, path2, node2)):
        return -1

        # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


# Find the node path from root node to given root fo the tree, save the path on the list,
# return true if path exists otherwise false
def findnode(root, path, k):
    if root is None:
        return False

    # Store this node is path vector.
    path.append(root.key)

    # Check if the k is same as root's key
    if root.key == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findnode(root.left, path, k)) or
            (root.right != None and findnode(root.right, path, k))):
        return True

    # If not present in subtree rooted with root,
    # remove root from path and return False

    path.pop()
    return False


# Please UnComment following lines to see Display Direct print Output
# node1 = 6
# node2 = 7
# t = lca(rootNode, node1, node2)
# print("lca of %d and %d is %d" % (node1, node2, t))
#
# node1 = 3
# node2 = 7
# t = lca(rootNode, node1, node2)
# print("lca of %d and %d is %d" % (node1, node2, t))
