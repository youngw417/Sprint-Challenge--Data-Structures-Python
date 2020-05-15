class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        

        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                current = self.left
                current.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                current = self.right
                current.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else: 
                current = self.left
                return current.contains(target)
        else:
            if not self.right:
                return False
            else: 
                current = self.right
                return current.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        current_max = self.value
        if self.right:
            current = self.right
            return current.get_max()
        else:
            return current_max

        # current_max = self.value
        # current = self.right
        # while current:
        #     if current_max < current.value:
        #         current_max = current.value
        #     current = current.right
        
        # return current_max
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            # fn(self.right.value)
            current = self.right
            current.for_each(fn)
        
        if self.left:
            # fn(self.left.value)
            current = self.left
            current.for_each(fn)

        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
#     Algorithm Inorder(tree)
#    1. Traverse the left subtree, i.e., call Inorder(left-subtree)
#    2. Visit the root.
#    3. Traverse the right subtree, i.e., call Inorder(right-subtree)
   
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        nodes = []
        nodes.append(node)
        while len(nodes) is not 0:
            my_node = nodes.pop(0)
            print(my_node.value)
            if my_node.left:
                nodes.append(my_node.left)
            if my_node.right:
                nodes.append(my_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        nodes = []
        nodes.append(node)
        while len(nodes) is not 0:
            my_node = nodes.pop(0)
            print(my_node.value)
           
            if my_node.right:
                nodes.insert(0, my_node.right)
            if my_node.left:
                nodes.insert(0, my_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
 