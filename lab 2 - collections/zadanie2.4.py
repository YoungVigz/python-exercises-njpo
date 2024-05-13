from collections import namedtuple

Node = namedtuple('Node', ['value', 'left', 'right'])

def insert_node(root, value):
    if root is None:
        return Node(value, None, None)
    
    if value < root.value:
        left_child = insert_node(root.left, value)
        return Node(root.value, left_child, root.right)
    else:
        right_child = insert_node(root.right, value)
        return Node(root.value, root.left, right_child)

def build_binary_tree(values):
    root = None
    for value in values:
        root = insert_node(root, value)
    return root

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print(' ' * level * 4, root.value)
        print_tree(root.left, level + 1)

values = [5, 3, 7, 2, 4, 6, 8]
values2 = [8, 16, 7, 2, 45, 6, 81]
root = build_binary_tree(values)
print_tree(root)

root2 = build_binary_tree(values2)
print_tree(root2)