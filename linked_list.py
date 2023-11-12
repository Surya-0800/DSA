class Node:
    def __init__(self,key,) -> None:
        self.key = key
        self.next = None


def displayList(head):
    curr = head
    while curr != None:
        print(curr.key)
        curr = curr.next

def getCount(head_node):
    curr = head_node
    count = 0
    while curr != None:
        count+=1
        curr = curr.next

    return count
def searchLinkedList(head,x):
    curr =head
    while curr != None:
        if x == curr.key:
            return 1
        curr = curr.next
    return 0

def insert_begin(head,x):
    curr = head.key
    head = Node(x)
    head.next = curr
    print(head.next)

def insert_end(head,x):
    curr = head
    while curr != None:
        curr = curr.next
    curr.next = Node(x)

def insert_postion(head,pos,x):
    curr = head
    count = 0
    temp = Node(x)
    if pos == 1:
        temp.next = head
        return temp
    curr = head
    for i in range(pos-2):
        curr = curr.next

    temp.next = curr.next
    curr.next = temp

def insert_sorted(head,x):
    temp = Node(x)
    curr = head
    while curr.next != None:
        b = curr.next.key
        if x > curr.key and x < b:
            print(curr.key,x,b)
            temp.next = curr.next
            curr.next = temp
        curr = curr.next
    new = head
    while new != None:
        print(new.key)
        new = new.next



head = Node(10)
head.next = Node(15)
head.next.next = Node(30)

# insert_begin(head,5)
# displayList(head)
# (insert_sorted(head,20))


li = [1,2,3,4,5,6]
li.pop()
print(li)