
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def _add_node(self, data, next=None):
        self.size += 1
        return Node(data, next)

    def insertAtBegining(self, data):
        self.head = self._add_node(data, self.head)

    def insertAtEnd(self, data):
        if self.isEmpty():
            return self.insertAtBegining(data)

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = self._add_node(data)

    def insertAt(self, data, index):
        if index == 0:
            return self.insertAtBegining(data)

        if index == self.size:
            return self.insertAtEnd(data)

        node = self.getNode(index-1)
        node.next = self._add_node(data, node.next)

    def insertMany(self, data, index):
        pass

    def update(self, data, index):
        self.getNode(index).data = data

    def removeAtBegining(self):
        self.head = self.head and self.head.next

    def removeAtEnd(self):
        if self.size == 0:
            return

        if self.size == 1:
            return self.removeAtBegining()

        self.getNode(self.size - 2).next = None

    def removeAt(self, data, index):
        if index == 0:
            return self.removeAtBegining()
        if index == self.size - 1:
            return self.removeAtEnd()

        node = self.getNode(index - 1)
        node.next = node.next.next

    def removeDuplicate(self):
        pass

    def contains(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def getFirst(self):
        return self.head and self.head.data

    def getLast(self):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        return last_node.data

    def get(self, index, default=None):
        if self.isEmpty():
            return default

        try:
            return self.getNode(index).data
        except IndexError:
            return default

    def getNode(self, index):
        self.checkIndexExists(index)
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def indexOf(self, data):
        node = self.head
        index = 0
        while node:
            if data == node.data:
                return index
            index += 1
            node = node.next

        raise ValueError(f"Value : {data} dose not exist in list")

    def getSize():
        return self.size

    def sort(self):
        pass

    def reverse(self):
        pass

    def toList(self):
        data = []
        last_node = self.head
        while last_node:
            data.append(last_node.data)
            last_node = last_node.next
        return data

    def print(self):
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next

    def isEmpty(self):
        if self.head is None:
            print("Linked list is empty")
            return True
        return False

    def checkIndexExists(self, index):
        if self.size <= index:
            raise IndexError(f"Index {index} is out of range")
        return True


