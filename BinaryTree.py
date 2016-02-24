"""
This is a binary tree module
in python using classes

Safe to use the Tree with
any object
"""

class BinaryTreeNode (object):
    def __init__(self, value):
        """
        Initializes a Node for a
        Binary tree

        Parameters
        value   (object): The value given to the new Node itself
        """

        self.value = value
        self.left  = None
        self.right = None

class BinaryTree (object):
    """ Class Variables """
    traversalString = ""

    """ Class Methods """
    def __init__(self, value = None):
        """
        Initializes the Binary Tree
        using the value passed

        Parameters
        value   (object): The value given to the root Node
        """

        if value is None:
            self.root = None
        else:
            self.root = BinaryTreeNode(value)

    def __str__(self):
        """
        Converts the tree into a string object
        through an in order traversal

        Return
        -> "Tree is Empty" if tree is empty
        -> String Object of the Tree
        """

        if self.root is None:
            return "Tree is Empty"
        else:
            self._inOrderTraversal(self.root)

        """ Reset the string for further calls """
        returnString = self.traversalString[0:-1] # Last Element is a space
        self.traversalString = ""

        return returnString

    def _inOrderTraversal(self, node):
        """
        Recursive method for getting a
        string from an in order traversal
        of the tree

        Return
        -> String ordered as per an in order traversal of tree

        Parameters
        node    (BinaryTreeNode): Node at which traversal begins
        """

        if node.left is not None:
            self._inOrderTraversal(node.left)

        self.traversalString = self.traversalString + str(node.value) + " "

        if node.right is not None:
            self._inOrderTraversal(node.right)

    def add(self, value):
        """
        Wrapper method for calling the recursive
        adding method '_add'

        Return
        -> Root Node and value added to it
        -> Node and value returned by _add

        Parameters
        value   (object): The value to be added to the tree
        """

        if self.root is None:
            self.root = BinaryTreeNode(value)
            return self.root, value
        else:
            return self._add(value, self.root)

    def _add(self, value, node):
        """
        Adds a value to the Binary tree
        using the value passed by recursion

        Return
        -> None is value is None
        -> Node at which value is inserted, and the value added

        Parameters
        value           (object): The value to be added to the tree
        node    (BinaryTreeNode): The Binary Tree Node at which value
                                  has to be added
        """

        # Add value to the node passed
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
                return node.left, value
            else:
                return self._add(value, node.left)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
                return node.right, value
            else:
                return self._add(value, node.right)




if __name__ != "__main__":
    exit(0)

numbers = BinaryTree()
node, value = numbers.add(5)
node, value = numbers.add(4)
node, value = numbers.add(3)
node, value = numbers.add(6)
node, value = numbers.add(7)
print numbers
