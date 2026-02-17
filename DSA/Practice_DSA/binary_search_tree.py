class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # Traversals
    #Left → Root → Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    #Root → Left → Right
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    #Left → Right → Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

    # Professional side view display
    def display_sideways(self, node, prefix="", is_left=True):
        if node is not None:

            if node.right:
                new_prefix = prefix + ("│   " if is_left else "    ")
                self.display_sideways(node.right, new_prefix, False)

            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))

            if node.left:
                new_prefix = prefix + ("    " if is_left else "│   ")
                self.display_sideways(node.left, new_prefix, True)


# -------- MAIN --------

tree = BinaryTree()

try:
    n = int(input("How many values? "))

    for i in range(n):
        val = int(input(f"Enter value {i+1}: "))
        tree.insert(val)

    while True:

        print("\nChoose an option:")
        print("1. Display tree (side view)")
        print("2. In-order")
        print("3. Pre-order")
        print("4. Post-order")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("\nBinary Search Tree:\n")
            tree.display_sideways(tree.root)

        elif choice == 2:
            print("\nIn-order:")
            tree.inorder(tree.root)
            print()

        elif choice == 3:
            print("\nPre-order:")
            tree.preorder(tree.root)
            print()

        elif choice == 4:
            print("\nPost-order:")
            tree.postorder(tree.root)
            print()

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice")

except KeyboardInterrupt:
    print("\nProgram stopped safely.")
except ValueError:
    print("Invalid input.")

"""
Recursion is a programming technique where a function calls itself to solve smaller instances of a problem until it reaches a base case. 
Essentially, it breaks a complex problem into simpler, more manageable subproblems.

Recursion is widely used in AI for tasks like tree searches, graph traversal, and problem-solving algorithms. I
n AI, it appears in algorithms such as Minimax for decision-making in games, backtracking for constraint satisfaction problems like Sudoku or n-queens,
and in recursive neural networks, which process hierarchical or structured data like natural language parsing or sentiment analysis. 
By breaking problems into smaller subproblems, recursion allows AI systems to systematically explore possibilities and handle complex data structures efficiently.

"""

"""
A binary tree is a hierarchical structure where each node has at most two children (left and right). 
The insertion logic ensures that for any node, the left child has a smaller value, and the right child has a larger value. 
This allows search operations to efficiently navigate the tree, cutting the search space in half at each step (O(log n) in a balanced tree).
Traversal methods use recursion because each subtree is itself a smaller binary tree.

In-order traversal: Visits nodes in ascending order.
Pre-order traversal: Visits the root before children (useful for copying or saving the tree structure).
Post-order traversal: Visits children before the root (useful for deletion or evaluating expressions).

Uses in AI

Binary trees and their search/traversal patterns are heavily used in AI:
Game trees: AI in games like chess or tic-tac-toe uses binary (or n-ary) trees to represent possible moves and outcomes. Recursive traversal evaluates which moves are optimal using algorithms like Minimax.
Decision trees: A fundamental AI tool for classification or regression. Each node represents a decision based on features, and traversing from root to leaf predicts outcomes.

Expression parsing: Recursive trees are used to evaluate mathematical or logical expressions, common in symbolic AI.
Pathfinding and reasoning: Recursive tree structures represent hierarchical plans or state spaces, making it easier for AI to explore possibilities efficiently.
"""
