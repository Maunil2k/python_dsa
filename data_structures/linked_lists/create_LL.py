class Node():
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class LinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is not None:
            tmp = self.head
            self.head = Node(data)
            self.head.next = tmp
        else:
            self.head = Node(data)

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = Node(data)

    def insert(self, data, index):
        pass

    def print_LL(self):
        current = self.head
        while current.data is not None:
            print(current.data)
            if current.next is not None:
                current = current.next
            else:
                current.data = None

if __name__ == "__main__":
    LL = LinkedList()
    LL.push(1)
    LL.push(2)
    LL.push(3)
    LL.push(4)
    LL.push(5)
    LL.append(4)
    LL.append(3)
    LL.append(2)
    LL.append(1)
    LL.print_LL()