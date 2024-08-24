from collections import deque


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    queue = deque([root])

    while queue:
        temp = queue.popleft()

        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)

        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)

    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("Inorder traversal before insertion: ", end="")
    inorder(root)
    print()

    key = 6
    root = insert(root, key)

    print("Inorder traversal after insertion: ", end="")
    inorder(root)
    print()
