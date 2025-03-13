import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def length(self):
        return self.size

    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        value = self._iter_node.value
        self._iter_node = self._iter_node.next
        return value

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements


if __name__ == "__main__":
    linked_list = LinkedList()
    for _ in range(10):
        linked_list.append(random.randint(1, 100))

    print("Länge der Liste:", linked_list.length())
    print("Elemente der Liste:", linked_list.display())

    print("Iterator-Durchlauf:")
    for value in linked_list:
        print(value, end=" ")
