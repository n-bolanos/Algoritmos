"""This file defines the class BST as a data structure made up by nodes"""
class TreeNode:
    """
    Class used as the base of other complex structures
    """
    def __init__(self, parent, value):
        self.parent: TreeNode | None = parent
        self.key = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None


class BinarySearchTree:
    def __init__(self, root: None | TreeNode = None):
        self.root = root

    # Operations on BST
    def search(self, x: TreeNode | None, k):
        ruta = []
        encontrado = False

        while x is not None and k != x.key:
            ruta.insert(0, x.key)
            if k < x.key:
                x = x.left
            else:
                x = x.right
            
        if x is not None:
            ruta.insert(0, x.key)
            if x.key == k:
                encontrado = True

        if not encontrado:
            return None

        return ruta

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

    def print_tree(self, node: TreeNode | None):
        if node is None:
            return ""
        else:
            return "{" + str(node.key) + self.print_tree(node.left) + self.print_tree(node.right) + "}"


arbol = BinarySearchTree()
valores = [int(i) for i in input().split()]
busqueda = int(input())

raiz = TreeNode(None, valores[0])
arbol.insert(raiz)

for index in range(1, len(valores)):
    nodo = TreeNode(None, valores[index])
    arbol.insert(nodo)

print(arbol.print_tree(raiz))


ruta = arbol.search(raiz, busqueda)

if ruta is not None:
    print(*ruta)
else:
    print("None")
