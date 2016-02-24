"""
This is a industry class binary
tree module in python

Safe to use the Tree with any
object
"""

class BinaryTreeNode (object):
    def __init__(self, value):
        """
        Initializes a Node for a Binary
        tree.

        Node contains a value, a left
        child and a right child

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

        returnString = self.orderTraversal()

        if returnString is None:
            return "Tree is Empty"
        else:
            return returnString

    def orderTraversal(self, traversalType = "in"):
        """
        Wrapper method for calling the recursive
        traversing method '_orderTraversal'

        Return
        -> None if root node is None
        -> String ordered as per the type passed

        Parameters
        traversalType   (string): Type of traversal. Read below
                                  for further information
        """

        if self.root is None:
            return None

        if traversalType in ("in", "pre", "post"):
            self._orderTraversal(self.root, traversalType)
        else:
            return None

        """ Reset the string for further calls """
        returnString = self.traversalString[0:-1] # Last Element is a space
        self.traversalString = ""

        return returnString

    def _orderTraversal(self, node, traversalType):
        """
        Recursive method for getting a
        string from a traversal of the
        tree

        Return
        -> String ordered as per a traversal of tree

        Parameters
        node    (BinaryTreeNode): Node at which traversal begins
        traversalType   (string): Type of traversal to be performed
                                  "in"  : In-Order Traversal
                                  "pre" : Pre-Order Traversal
                                  "post": Post-Order Traversal
        """

        if traversalType == "pre":
            self.traversalString = self.traversalString + str(node.value) + " "

        if node.left is not None:
            self._orderTraversal(node.left, traversalType)

        if traversalType == "in":
            self.traversalString = self.traversalString + str(node.value) + " "

        if node.right is not None:
            self._orderTraversal(node.right, traversalType)

        if traversalType == "post":
            self.traversalString = self.traversalString + str(node.value) + " "

    def add(self, value):
        """
        Wrapper method for calling the recursive
        adding method '_add'

        Return
        -> Root Node
        -> Node returned by _add

        Parameters
        value   (object): The value to be added to the tree
        """

        if self.root is None:
            self.root = BinaryTreeNode(value)
            return self.root
        else:
            return self._add(value, self.root)

    def _add(self, value, node):
        """
        Adds a value to the Binary tree
        using the value passed by recursion

        Return
        -> None is value is None
        -> Node at which value is inserted

        Parameters
        value           (object): The value to be added to the tree
        node    (BinaryTreeNode): The Binary Tree Node at which value
                                  has to be added
        """

        # Add value to the node passed
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
                return node.left
            else:
                return self._add(value, node.left)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
                return node.right
            else:
                return self._add(value, node.right)

    def find(self, value):
        """
        Wrapper method for calling the recursive
        find method '_find'

        Return
        -> None if root node is None
        -> Node returned by _find

        Parameters
        value   (object): The value to be searched for in the tree
        """

        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    def _find(self, value, node):
        """
        Finds a value in the Binary tree
        using the value passed by recursion

        Return
        -> None if search is unsuccessful
        -> Node at which value is found

        Parameters
        value           (object): The value to be added to the tree
        node    (BinaryTreeNode): The Binary Tree Node at which value
                                  has to be added
        """

        if value == node.value:
            return node
        elif value < node.value:
            if node.left is None:
                return None
            else:
                return self._find(value, node.left)
        else:
            if node.right is None:
                return None
            else:
                return self._find(value, node.right)



if __name__ != "__main__":
    exit(0)

numbers = BinaryTree()
node, value = numbers.add(5)
node, value = numbers.add(4)
node, value = numbers.add(3)
node, value = numbers.add(6)
node, value = numbers.add(7)
if numbers.find(7):
    print numbers
