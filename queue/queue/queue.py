class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0  # size of queue
        self.left = 0  # 0 means deletion, 0 at left means deleting at left  side of queue
        self.right = 1  # 1 means addition, 1 at right means adding at right side of queue

    def append(self, data):
        temp = Node(data)
        if self.__size == 0:
            self.head = temp
            self.tail = temp
            self.__size += 1
        else:
            if self.right:
                self.tail.next = temp
                temp.prev = self.tail
                self.__size += 1
                self.tail = temp
            else:
                self.head.prev = temp
                temp.next = self.head
                self.head = temp
                self.__size += 1

    def __len__(self):
        return self.__size

    def __repr__(self):
        current = self.head
        string = 'Empty'
        c = 0
        while current:
            if c == 0:
                if self.__size == 0:
                    return string
                else:
                    string = str(current.data)
                    current = current.next
                    c += 1
            else:
                string += ', ' + str(current.data)
                current = current.next
        return string

    def mode(self, left=0, right=1):
        self.left = int(left)
        self.right = int(right)
        return '(' + str(self.left)+', '+str(self.right)+')'

    def pop(self):
        if self.__size > 0:
            if self.right:
                data = self.head.data
                next = self.head.next
                next.prev = None
                self.head = next
            else:
                data = self.tail.data
                prev = self.tail.prev
                prev.next = None
                self.tail = prev
            self.__size -= 1
            return data
        else:
            raise IndexError("Queue is empty")

    def __contains__(self, item):
        current = self.head
        while current:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
        raise StopIteration

    def index(self, data):
        current = self.head
        c = 0
        while current:
            if current.data == data:
                return c
            else:
                current = current.next
                c += 1
        return None
