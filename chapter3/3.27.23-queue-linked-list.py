class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def __str__(self):
        return str(self.data)




class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def pop(self):
        current = self.head
        if current.getNext is None:
            self.remove(current)

        tail = current.getNext is None
        while not tail:
            previous, current = current, current.getNext()
            tail = current.getNext() is None
        previous.setNext(None)
        return current

    def print(self):
        current = self.head
        tail = current.getNext is None
        while not tail:
            print(current)
            current = current.getNext()
            tail = current is None


class Queue:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return self.items.size()

    def print(self):
        self.items.print()


mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
print('before pop')
mylist.print()
mylist.pop()
print('before pop')
mylist.print()


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
print('before dequeue')
q.print()
tail = q.dequeue()
print('after dequeue')
q.print()
print('poped item : %s'%tail)