class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.isempty():
            return 'Stack empty'
        else:
            return self.top.data
        
    def pop(self):
        if self.top is None:
            return 'Stack empty'
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

    def size(self):
        temp = self.top
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

s = stack()

def reverse_str(text):
    s = stack()
    for i in text:
        s.push(i)
    res = ""
    while not s.isempty():
        res += s.pop()
    print(res)

def text_editor(text, pattern):
    u = stack()
    r = stack()
    for i in text:
        u.push(i)
    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    res = ""
    while not u.isempty():
        res = u.pop() + res
    print(res)

L = [
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0]
]

def find_celeb(L):
    s = stack()
    for i in range(len(L)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        if L[i][j] == 0:
            s.push(i)
        else:
            s.push(j)
    print(s.traverse())

find_celeb(L)
