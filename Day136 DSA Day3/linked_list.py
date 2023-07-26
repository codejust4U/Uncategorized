class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

    
class Linked_list:

    # creation of linked list
    def __init__(Self):
        # empty linked list
        Self.head = None
        Self.n = 0

    # len method

    def __len__(self):
        return self.n

    # operations on linked list

    # 1. Insertion
    def insert_head(self, value):
        # new node
        new_node = Node(value)

        # connection
        new_node.next = self.head
        # reassign
        self.head = new_node
        # increment n
        self.n = self.n+1

    # Traversing

    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result = result+str(current.data)+'->'
            current = current.next
        return result[:-2]

    # append
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n+1
            return
        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node
        self.n = self.n+1

    # insert in somewhere middle
    def insert_mid(self, after, value):
        new_node = Node(value)
        current = self.head
        while current != None:
            if current.data == after:
                break
            current = current.next

        # case 1 - break - u got the item
        if current != None:
            new_node = current.next
            current.next = new_node
            self.n = self.n+1
        # case 2- loop runs and didnt get the item
        else:
            return 'Item not found'

        # clearing
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return 'Empty linked list'
        self.head = self.head.next
        self.n = self.n-1

    def pop(self):
        if self.head ==None:
            return 'Empyt linked list'
        current = self.head
        # if linked list has one item
        if current.next == None:
            # head is the last item
            return self.delete_head()
            
        while current.next.next != None:
            current = current.next
        current.next = None
        self.n = self.n-1


    def remove(self,value):
        if self.head == None:
            return 'Empyt linked list'
        if self.head.data == value:
            # u want to remove head
            return self.delete_head()
        current = self.head
        while current.next != None:
            if current.next.data == value:
                break
            current = current.next
        # if we got the item
        # if we didnt get the item
        if current.next == None:
            return 'Item not found'
        else:
            current.next = current.next.next

    def search(self,item):
        current = self.head
        pos = 0
        while current!=None:
            if current.data == item:
                return pos
            current=current.next
            pos+=1
        return 'Element not found'
    
    #delete by index
    def __getitem__(self,index):
        current = self.head
        pos = 0
        while current!=None:
            if pos==index:

                return current.data
            current = current.next
            pos+=1
        return 'IndexError'


    

    # Traversing
    def __str__(self):
        current=self.head
        result=''
        while current!= None:
            result=result+str(current.data)+'->'
            current=current.next
        return result[:-2]
    
    # append
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n+1
            return
        current = self.head
        while current.next != None:
            current = current.next

        current.next = new_node
        self.n = self.n+1

    # insert in somewhere middle
    def insert_mid(self,after,value):
        new_node = Node(value)
        current = self.head
        while current!= None:
            if current.data == after:
                break
            current = current.next

        # case 1 - break - u got the item
        if current != None:
            new_node = current.next
            current.next = new_node
            self.n = self.n+1
        #case 2- loop runs and didnt get the item
        else:
            return 'Item not found'
        
        # clearing
    def clear(self):
        self.head = None
        self.n = 0



L = Linked_list()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

len(L)


print(L)


print(L[4])

print(L)
