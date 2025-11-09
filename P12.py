class RBTNode:
    """
    Class used as the base of other complex structures
    """
    def __init__(self, value, parent = None):

        self.parent: RBTNode|None = parent
        self.key = value
        self.left: RBTNode|None = None
        self.right: RBTNode|None = None
        self._color = 'RED'

    def __eq__(self, value: 'RBTNode') -> bool:
        return self.key == value.key

class RBTNIL (RBTNode):
    def __init__(self):
        super().__init__(None, None)
        self._color = 'BLACK'


class RedBlackTree:
    def __init__(self, root: RBTNode | None = None):
        self.NIL = RBTNIL()
        
        if root is not None:
            self.root: RBTNode = root
        else:
            self.root: RBTNode = self.NIL
        
    def search(self, x: RBTNode, k):
        while x != self.NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def minimum(self, x: RBTNode):
        while x.left != self.NIL:
            x = x.left
        return x

    def insert(self, z: RBTNode):
        """
        This function allows to insert a new node into the tree
        """
        x = self.root
        y = self.NIL

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        
        z.left = self.NIL
        z.right = self.NIL
        z._color = 'RED'

        self.insert_fixup(z)

    def _left_rotate(self, x: RBTNode):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x: RBTNode):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y

    def insert_fixup(self, z:RBTNode):
        while z.parent._color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y._color == 'RED':
                    z.parent._color = 'BLACK'
                    y._color = 'BLACK'
                    z.parent.parent._color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent._color = 'BLACK'
                    z.parent.parent._color = 'RED'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y._color == 'RED':
                    z.parent._color = 'BLACK'
                    y._color = 'BLACK'
                    z.parent.parent._color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent._color = 'BLACK'
                    z.parent.parent._color = 'RED'
                    self._left_rotate(z.parent.parent)
        self.root._color = 'BLACK'


    def _transplant(self, u:RBTNode, v:RBTNode):
        """
        Auxiliary function to replace a subtree rooted at u with the subtree rooted at v
        """
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent
    
    def delete(self, z: RBTNode):
        """
        This function allows to delete any existing node in the tree
        """
        y = z
        y_original_color = y._color

        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y._color
            x = y.right
            if y != z.right:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            else:
                x.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y._color = z._color
        
        if y_original_color == 'BLACK':
            self.delete_fixup(x)
        
    def delete_fixup(self, x:RBTNode):
        while x != self.root and x._color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w._color == 'RED':
                    w._color = 'BLACK'
                    x.parent._color = 'RED'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left._color == 'BLACK' and w.right._color == 'BLACK':
                    w._color = 'RED'
                    x = x.parent
                else:
                    if w.right._color == 'BLACK':
                        w.left._color = 'BLACK'
                        w._color = 'RED'
                        self._right_rotate(w)
                        w = x.parent.right
                    w._color = x.parent._color
                    x.parent._color = 'BLACK'
                    w.right._color = 'BLACK'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w._color == 'RED':
                    w._color = 'BLACK'
                    x.parent._color = 'RED'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.left._color == 'BLACK' and w.right._color == 'BLACK':
                    w._color = 'RED'
                    x = x.parent
                else:
                    if w.left._color == 'BLACK':
                        w.right._color = 'BLACK'
                        w._color = 'RED'
                        self._left_rotate(w)
                        w = x.parent.left
                    w._color = x.parent._color
                    x.parent._color = 'BLACK'
                    w.left._color = 'BLACK'
                    self._right_rotate(x.parent)
                    x = self.root
        x._color = 'BLACK'

    def printTree(self, x:RBTNode):
        if x == self.NIL:
            return ""
        else:
            if x._color == 'BLACK':
                nodo = "{" + str(x.key) + "#"
            else:
                nodo = "{" + str(x.key) + "®"
            return nodo + self.printTree(x.left) + self.printTree(x.right) + "}"
        

lista = [int(i) for i in input().split()]
borrar = [int(i) for i in input().split()]
arbol = RedBlackTree()
for element in lista:
    nodo = RBTNode(element)
    arbol.insert(nodo)

print(arbol.printTree(arbol.root))

for element in borrar:
    nodo = arbol.search(arbol.root, element)
    arbol.delete(nodo)
    print(arbol.printTree(arbol.root))

