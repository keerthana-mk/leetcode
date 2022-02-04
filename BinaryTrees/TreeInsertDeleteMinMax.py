class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def BSTInsertion(root, key):
        if root is None:
            return Node(key)
        if root.val == key:
            return root
        elif root.val < key:
            root.right = Node.BSTInsertion(root.right, key)
        elif root.val > key:
            root.left = Node.BSTInsertion(root.left, key)
        return root

    def BSTSearch(root, key):
        if root is None:
            return
        if root.val == key:
            return root
        # Key is greater than root
        elif root.val < key:
            return Node.BSTSearch(root.right, key)
        else:
            # Key is less than root
            return Node.BSTSearch(root.left, key)

    # Inorder Traversal Left -> Center -> Right
    def inorder(root):
        if root:
            Node.inorder(root.left)
            print(root.val, end=" ")
            Node.inorder(root.right)

    # obtain the min value of the BST
    # Note that the entire tree does not need to be searched
    # leftmost node contains the least value
    def BSTMinValueNode(root):
        current_node = Node(root)
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # lerightmost  node contains the largest/max value
    def BSTMaxValueNode(root):
        current_node = Node(root)
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

    '''
    1) Node to be deleted is the leaf: Simply remove from the tree. 
    2) Node to be deleted has only one child: Copy the child to the node and delete the child 
    3) Node to be deleted has two children: Find inorder successor of the node. Copy contents of 
    the inorder successor to the node and delete the inorder successor. Note that inorder predecessor can also be used.
    The important thing to note is, inorder successor is needed only when the right child is not empty. In this particular case,
    inorder successor can be obtained by finding the minimum value in the right child of the node. 
    '''

    def BSTDeletion(root, key):
        if root is None:
            return root
        print("root.val=", root.val)
        # left subtree - if key < root
        if key < root.val:
            return Node.BSTDeletion(root.left, key)
        # right subtree - if key > root
        elif key > root.val:
            return Node.BSTDeletion(root.right, key)
        # if key == root then this is the node to be deleted
        else:
            # if node has no child or single child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children:
            # Get the inorder successor
            # (smallest in the right subtree)
            temp = Node.BSTMinValueNode(root.right)
            # print(temp.val)
            # Copy the inorder successor's content to this node
            root.val = temp.val
            # Delete the inorder successor
            root.right = Node.BSTDeletion(root.right, temp.val)
            print(("root deleted=", root))
        return root


r = Node(50)
r = Node.BSTInsertion(r, 30)
r = Node.BSTInsertion(r, 20)
r = Node.BSTInsertion(r, 40)
r = Node.BSTInsertion(r, 70)
r = Node.BSTInsertion(r, 60)
r = Node.BSTInsertion(r, 80)

Node.inorder(r)
Node.BSTSearch(r, 30)
new_root = Node.BSTDeletion(r, 50)
print()
Node.inorder(new_root)
