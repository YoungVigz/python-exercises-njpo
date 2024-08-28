import random
import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def __len__(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return max(left_height, right_height) + 1

    def count(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

    def __pow__(self, exponent):
        initial_count = self.count()
        target_count = initial_count ** exponent
        while self.count() < target_count:
            self << random.randint(1, 100)
        return self

    def __iter__(self):
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node.value
            yield from self._inorder_traversal(node.right)

    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is not None:
            yield node.value
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)

    def postorder_traversal(self):
        return self._postorder_traversal(self.root)

    def _postorder_traversal(self, node):
        if node is not None:
            yield from self._postorder_traversal(node.left)
            yield from self._postorder_traversal(node.right)
            yield node.value

    def __contains__(self, value):
        return self._find(self.root, value) is not None

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def __getitem__(self, value):
        node = self._find(self.root, value)
        if node:
            return node.value
        else:
            raise KeyError(f"Value {value} not found in tree")

    def __bool__(self):
        return self.root is not None

    def __setitem__(self, key, value):
        """Ustawia wartość w drzewie."""
        self.root = self._insert(self.root, key)

    def __lshift__(self, value):
        self.root = self._insert(self.root, value)
        return self

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def __str__(self):
        if not self.root:
            return '<empty tree>'
        return self._build_str(self.root, "", True)
    
    def _build_str(self, node, prefix, is_tail):
        result = prefix + ("└── " if is_tail else "├── ") + str(node.value) + "\n"
        if node.left or node.right:
            if node.left:
                result += self._build_str(node.left, prefix + ("    " if is_tail else "│   "), False if node.right else True)
            if node.right:
                result += self._build_str(node.right, prefix + ("    " if is_tail else "│   "), True)
        return result

    def __add__(self, other):
        new_tree = BinaryTree()
        for value in self:
            new_tree << value
        for value in other:
            new_tree << value
        return new_tree

    def __sub__(self, other):
        new_tree = BinaryTree()
        for value in self:
            if value not in other:
                new_tree << value
        return new_tree
