"""This file defines the class LinkedList as a data structure made up by nodes"""
from node import ListNode, Sentinel

class LinkedList:
    def __init__(self):
        self.head = Sentinel()

    def insert(self, value, y: ListNode) -> None:
        """
        This function inserts the value specified right after node 'y'
        """
        new = ListNode(value, y, y.next)
        y.next.prev = new
        y.next = new

    def delete(self, x:ListNode) -> None:
        """
        This function deletes a node from the linked list
        """
        if type(x) is Sentinel:
            raise Exception("It is not allowed to delete this node since it is a sentinel")
        
        x.prev.next = x.next
        x.next.prev = x.prev

    def search(self, k) -> ListNode | None:
        self.head.set_value(k)
        current = self.head.next

        while current.get_value() != k:
            current = current.next

        if type(current) is Sentinel:
            self.head.set_value(None)
            return None
        return current


    def print_ll(self):
        current = self.head.next

        if type(current) is Sentinel:
            print("Empty")
            return

        while type(current) is not Sentinel:
            print(current.get_value(), end=" ")
            current = current.next
        print("")

        
lista = LinkedList()
lista.insert(1, lista.head)
lista.insert(2, lista.head.next)
lista.insert(3, lista.head)
lista.delete(lista.head.prev)
lista.insert(4, lista.head)
print(lista.search(3))
print(lista.search(5))
lista.print_ll()