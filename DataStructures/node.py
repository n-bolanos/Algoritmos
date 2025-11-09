"""This file defines classes Node and Sentinel, used to form more complex data strucutres, as the serve as 
building blocks."""

class TreeNode:
    """
    Class used as the base of other complex structures
    """
    def __init__(self, parent, value):
        self.parent: TreeNode | None = parent
        self.key = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None



class ListNode:
    """Class used as the base of other complex structures"""
    def __init__(self, key, prev: 'ListNode', next: 'ListNode') :
        self._key = key
        self.prev = prev
        self.next = next

    def get_value(self):
        return self._key
    
    def set_value(self, key):
        self._key = key
        return

class Sentinel(ListNode):
    """Class used to mark the top and/or bottom of a structure (LinkedLists)"""
    
    def __init__(self) -> None:
        super().__init__("<SENTINEL>", self, self)
