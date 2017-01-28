#---------------------------------------------------------
# Anna Cho
# anna.cho@ischool.berkeley.edu
# Homework #3
# September 20, 2016
# BST.py
# BST
# ---------------------------------------------------------

class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right = None
        self.left = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root
    
    #These are "external functions" that will be called by your main program - I have given these to you
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def in_order_print(self):
        _in_order_print(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count +=1
        return
    if root.word > word:
        if root.left == None:
            root.left = Node(word)
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word)
        else:
            _add(root.right, word)
    
#Function to find word in tree
def _find(root, word):
    if root is None:    # word is not in the tree
        return 0
    if root.word == word:   # word has been found
        return root.count
    if root.word > word:
        return _find(root.left, word)
    if root.word < word:
        return _find(root.right, word)

#Get number of nodes in tree
def _size(root):
    if root is None:   # Leaf nodes
        return 0
    else:   # Root node and its children
        return 1 + _size(root.left) + _size(root.right) 

#Get height of tree
def _height(root):
    if root is None:
        return 0    # Leaf node
    else:
        return max(_height(root.left) + 1, _height(root.right) + 1) # Returns the longest path
    
#Function to print tree in order
def _in_order_print(root):
    if not root:
        return
    _in_order_print(root.left)
    print(root.word)
    print(root.count)
    _in_order_print(root.right)
