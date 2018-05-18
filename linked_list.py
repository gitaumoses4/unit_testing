class Node:
    data = None
    nextNode = None

    def __init__(self, data):
        self.data = data


class LinkedList:
    size = 0

    def __init__(self):
        self.head = None

    def clear(self):
        self.head = None
        self.size = 0

    def empty(self):
        # check whether the linked list is empty
        return self.head is None

    def length(self):
        # returns the length of the linked list
        return self.size

    def insert(self, data):
        # inserts an element into the linked list
        self.size += 1
        if self.head is None:
            self.head = Node(data)
        else:
            n = Node(data)
            temp = self.head

            self.head = n
            self.head.nextNode = temp

    def delete(self, data):
        # deletes an item from the linked list
        if self.empty():
            return False
        else:
            if self.head.data == data:
                self.head = self.head.nextNode
            else:
                temp = self.head
                while temp.nextNode is not None:
                    if temp.nextNode.data is data:
                        temp.nextNode = temp.nextNode.nextNode
                        return True

                    temp = temp.nextNode
            return False

    def find(self, data):
        # checks if an element exists in the linked list
        temp = self.head
        while temp is not None:
            if temp.data is data:
                return True
            temp = temp.nextNode

        return False

    def to_list(self):
        m_list = []
        temp = self.head
        while temp is not None:
            m_list.append(temp.data)
            temp = temp.nextNode
        m_list.reverse()
        return m_list


if __name__ == '__main__':
    items = [1, 3, 5, 7, 4, 2]
    linked_list = LinkedList()

    for item in items:
        linked_list.insert(item)

    linked_list.delete(7)
    print(linked_list.to_list())
