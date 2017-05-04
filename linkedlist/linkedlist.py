class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self, a1=[]):
        self.__head = None
        self.__size = 0
        self.__current = None
        for i in a1:
            self.append(i)

    def append(self, data):
        temp = Node(data)
        if self.__size == 0:
            self.__head = temp
            self.__current = temp
            self.__size += 1
        else:
            temp.prev = self.__current
            self.__current.next = temp
            self.__current = temp
            self.__size += 1

    def __repr__(self):
        current = self.__head
        c = 0
        a2 = "[]"
        while current:
            if c == 0:
                if c == self.__size-1:
                    a2 = "[" + str(current.data) + "]"
                elif c == self.__size:
                    return a2
                else:
                    c += 1
                    a2 = "[" + str(current.data)
            elif c == self.__size-1:
                a2 += ", " + str(current.data) + "]"
            else:
                a2 += ", " + str(current.data)
                c += 1
            current = current.next
        return a2

    def __len__(self):
        return self.__size

    def __iter__(self):
        current = self.__head
        while current:
            yield current.data
            current = current.next
        raise StopIteration

    def __contains__(self, item):
        current = self.__head
        while current:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def delete(self, data):
        current = self.__head
        prev = None
        found = False
        while current:
            if current.data == data:
                found = True
                self.__size -= 1
                break
            else:
                prev = current
                current = current.next
        if found:
            if prev:
                if not current.next:
                    prev.next = None
                    self.__current = prev
                else:
                    prev.prev = current.prev
                    prev.next = current.next
            else:
                self.__head = current.next

    def is_empty(self):
        head = self.__head
        if not head:
            return True
        else:
            return False

    def insert(self, index, data):
        current = self.__head
        temp = Node(data)
        i = 0
        if len(self) == 0:
            if index == 0:
                self.append(data)
        elif index == 0:
            temp.next = self.__head
            self.__head.prev = temp
            self.__head = temp
            self.__size += 1
        elif index > len(self)-1:
            raise IndexError("List out of range")
        else:
            while current:
                if index == i:
                    prev = current.prev
                    prev.next = temp
                    temp.next = current
                    temp.prev = prev
                    current.prev = temp
                    self.__size += 1
                    break
                current = current.next
                i += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty list')
        current = self.__current
        a = current.data
        prev = current.prev
        if prev:
            prev.next = None
            self.__size -= 1
            self.__current = prev
            return a
        else:
            head = self.__head
            self.delete(head.data)
        return a

    def head1(self):
        return self.__head.data

    def extend(self, d=[]):
        for i in d:
            self.append(i)

    def index(self, data):
        current = self.__head
        i = 0
        while current:
            if current.data == data:
                return i
            else:
                current = current.next
                i += 1
        return False

