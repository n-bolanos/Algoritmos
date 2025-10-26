"""This file defines classes Node and Sentinel, used to form more complex data strucutres, as the serve as 
building blocks."""

class Node:
    """Class used as the base of other complex structures"""
    def __init__(self, key, prev: 'Node', next: 'Node') :
        self._key = key
        self.prev = prev
        self.next = next

    def get_value(self):
        return self._key
    
    def set_value(self, key):
        self._key = key
        return

class Sentinel(Node):
    """Class used to mark the top and/or bottom of a structure (LinkedLists)"""
    
    def __init__(self) -> None:
        super().__init__("<SENTINEL>", self, self)
