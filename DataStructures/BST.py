"""This file defines the class BST as a data structure made up by nodes"""
from node import TreeNode

class BinarySearchTree:
    def __init__(self, root: None | TreeNode = None):
        self.root = root

    #Tree walks
    def in_order(self, z:TreeNode|None):
        if z is not None:
            self.in_order(z.left)
            print(z.key, end=" ")
            self.in_order(z.right)

    def pre_order(self, z:TreeNode|None):
        if z is not None:
            print(z.key, end=" ")
            self.pre_order(z.left)
            self.pre_order(z.right)
            
    def pos_order(self, z:TreeNode|None):
        if z is not None:
            self.pos_order(z.left)
            self.pos_order(z.right)
            print(z.key, end=" ")

    # Available search queries

    def search(self, x: TreeNode | None, k):
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def minimum(self, x: TreeNode):
        while x.left is not None:
            x = x.left # type: ignore
        return x
    
    def maximum(self, x: TreeNode):
        while x.right is not None:
            x = x.right # type: ignore
        return x
    
    def successor(self, x: TreeNode):
        if x.right is None:
            return self.minimum(x.right) # type: ignore
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y
    
    def predecessor(self, x: TreeNode):
        if x.left is None:
            return self.maximum(x.left) # type: ignore
        y = x.parent
        while y is not None and x == y.left:
            x = y
            y = y.parent
        return y

    # Operations on BST

    def insert(self, z: TreeNode):
        """
        This function allows to insert a new node into the tree
        """
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def _transplant(self, u:TreeNode, v:TreeNode|None):
        """
        Auxiliary function to replace a subtree rooted at u with the subtree rooted at v
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent
    
    def delete(self, z: TreeNode):
        """
        This function allows to delete any existing node in the tree
        """
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y != z.right:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
        


if __name__ == '__main__':
    arbol = BinarySearchTree()
    raiz = TreeNode(None, 10)
    nodo1 = TreeNode(None, 1)
    nodo2 = TreeNode(None, 100)
    nodo3 = TreeNode(None, 50)
    nodo4 = TreeNode(None, 7)
    arbol.insert(raiz)
    arbol.insert(nodo1)
    arbol.insert(nodo2)
    arbol.insert(nodo3)
    arbol.insert(nodo4)
    arbol.delete(raiz)
    arbol.in_order(arbol.root)
    print()
    arbol.pre_order(arbol.root)
