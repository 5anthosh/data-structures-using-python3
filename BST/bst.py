class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class Bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        temp = Node(data)
        if self.size == 0:
            self.root = temp
            self.size += 1
        else:
            current = self.root
            while current:
                if data == current.data:
                    string = str(data) + " is already available"
                    raise ValueError(string)
                elif data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = temp
                        temp.parent = current
                        self.size += 1
                        break
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = temp
                        temp.parent = current
                        self.size += 1
                        break

    def lookup(self, data):
        current = self.root
        if current:
            string = 'root' + '(' + str(self.root.data) + ')'
        else:
            return None
        while current:
            if data == current.data:
                return string
            if data > current.data:
                if current.right:
                    current = current.right
                    string += '-' + 'r' + '(' + str(current.data) + ')'
                else:
                    return None
            else:
                if current.left:
                    current = current.left
                    string += '-' + 'l' + '(' + str(current.data) + ')'
                else:
                    return None

    def __len__(self):
        return self.size

    def __contains__(self, item):
        current = self.root
        while current:
            if current.data == item:
                return True
            else:
                if item > current.data:
                    current = current.right
                else:
                    current = current.left
        return False

    def _inorder(self, node, string):
        if node:
            self._inorder(node.left, string)
            string.append(node.data)
            self._inorder(node.right, string)

    def _preorder(self, node, string):
        if node:
            string.append(node.data)
            self._preorder(node.left, string)
            self._preorder(node.right, string)

    def _postorder(self, node, string):
        if node:
            self._postorder(node.left, string)
            self._postorder(node.right, string)
            string.append(node.data)

    def order(self, order):
        string = []
        if order.startswith("in"):
            self._inorder(self.root, string)
        elif order.startswith("pre"):
            self._preorder(self.root, string)
        elif order.startswith("post"):
            self._postorder(self.root, string)
        return string

    def get_min(self):
        current = self.root
        while current:
            if current.left:
                current = current.left
            else:
                return current.data
        return None

    def get_max(self):
        current = self.root
        while current:
            if current.right:
                current = current.right
            else:
                return current.data

    def delete(self, data):
        current = self.root
        while current:
            if current.data == data:
                self.size -= 1
                break
            elif current.data < data:
                current = current.right
            elif current.data > data:
                current = current.left
        if current:
            parent = current.parent
            left = current.left
            right = current.right
            if left and right:
                current1 = right
                while current1:
                    if current1.left:
                        current1 = current1.left
                    else:
                        smallest = current1
                        break
                if right.data != smallest.data:
                    smallest.right = right
                    print(smallest.right.data)
                if left.data != smallest.data:
                    smallest.left = left
                if parent:
                    if current.data > parent.data:
                        parent.right = smallest
                    else:
                        parent.left = smallest
                else:
                    self.root = smallest
                parent1 = smallest.parent
                if parent1.data < smallest.data:
                    parent1.right = None
                else:
                    parent1.left = None
            elif left and not right:
                if parent:
                    if current.data > parent.data:
                        parent.right = left
                    else:
                        parent.left = left
                else:
                    self.root = left
            elif not left and right:
                if parent:
                    if current.data > parent.data:
                        parent.right = right
                    else:
                        parent.left = right
                else:
                    self.root = right
            elif not left and not right:
                if parent:
                    if current.data > parent.data:
                        parent.right = None
                    else:
                        parent.left = None
                else:
                    self.root = None
                    
if __name__ == '__main__':
    a = Bst()
    a.insert(23)
    a.insert(25)
    a.insert(24)
    a.insert(27)
    a.insert(26)
    a.insert(28)
    a.insert(22)
    print(a.lookup(28))
    a.delete(27)
    print(a.lookup(26))
