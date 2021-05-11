
class Node:
    """ A node of single linked list """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    """ Single linked list """

    def __init__(self):
        self.head = None
        self.size = 0

    def _add_node(self, data, next=None):
        """ init node to add it to list  """
        self.size += 1
        return Node(data, next)

    def insertAtBegining(self, data):
        """ Insert value at begining """
        self.head = self._add_node(data, self.head)
        return self

    def insertAtEnd(self, data):
        """ Insert value at end """
        if self.isEmpty():
            return self.insertAtBegining(data)

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = self._add_node(data)
        return self

    def insertAt(self, data, position):
        """ Insert value at specific position """
        if position == 0:
            return self.insertAtBegining(data)

        if position == self.size:
            return self.insertAtEnd(data)

        node = self.getNode(position-1)
        node.next = self._add_node(data, node.next)
        return self

    def insertManyAtBegining(self, data):
        """ Insert Multi values at begining """
        for i in range(1, len(data)+1):
            self.insertAtBegining(data[-i])
        return self

    def insertMany(self, data, position):
        """ Insert multi values at specific position """
        if position == 0:
            return self.insertManyAtBegining(data)

        node = self.getNode(position-1)
        for i in range(1, len(data)+1):
            node.next = self._add_node(data[-i], node.next)
        return self

    def update(self, data, index):
        """ Update value of specific index """
        self.getNode(index).data = data
        return self

    def removeFirst(self):
        """ Remove first item of list """
        if self.size == 0:
            return self

        self.head = self.head.next
        self.size -= 1
        return self

    def removeLast(self):
        """ Remove last item of list """
        if self.size <= 1:
            return self.removeFirst()

        self.getNode(self.size - 2).next = None
        self.size -= 1
        return self

    def removeAt(self, data, index):
        """ Remove item at specific position """
        if index == 0:
            return self.removeFirst()
        if index == self.size - 1:
            return self.removeLast()

        node = self.getNode(index - 1)
        node.next = node.next.next
        self.size -= 1
        return self

    def removeDuplicate(self):
        """ Remove duplicates values from array """
        hash = set()  # Hash to store seen values
        current = self.head
        while current.next:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return self

    def contains(self, data):
        """ Check if list contains specific value """
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def getFirst(self):
        """ Get value of first node """
        return self.head and self.head.data

    def getLast(self):
        """ Get value of last node """
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        return last_node.data

    def get(self, index, default=None):
        """ Get value of specific position, if node dose not exist then return :default value """
        if self.isEmpty():
            return default

        try:
            return self.getNode(index).data
        except IndexError:
            return default

    def getNode(self, index):
        """ Get node by index """
        self.checkIndexExists(index)
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def indexOf(self, data):
        """ Get index of node depends on value """
        node = self.head
        index = 0
        while node:
            if data == node.data:
                return index
            index += 1
            node = node.next

        raise ValueError(f"Value : {data} dose not exist in list")

    def getSize():
        """ Get size of list """
        return self.size

    def sort(self):
        """ Sort list """
        pass
        return self

    def reverse(self):
        """ Reverse list """
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self

    def toList(self):
        """ Return all items as list """
        data = []
        last_node = self.head
        while last_node:
            data.append(last_node.data)
            last_node = last_node.next
        return data

    def print(self):
        """ Print all items of list """
        last_node = self.head
        while last_node:
            print(last_node.data)
            last_node = last_node.next
        return self

    def isEmpty(self):
        """ Check if list is empty """
        if self.head is None:
            return True
        return False

    def checkIndexExists(self, index):
        """ Check if index exists in list """
        if self.size <= index:
            raise IndexError(f"Index {index} is out of range")
        return True

