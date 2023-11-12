class Node:
    def __init__(self,key,) -> None:
        self.key = key
        self.next = None

def traversal(head):
    if head == None:
        return head
    print(head.key)
    curr = head.next
    while curr != head:
        print(curr.key)
        curr = curr.next

def insert_cll(head,x):
    temp = Node(x)
    if head == None:
        temp.next = head
    curr = head
    temp.next = head.next
    head.next = temp
    temp.key,head.key = head.key,temp.key

head = Node(10)
head.next = Node(15)
head.next.next = Node(30)
head.next.next.next = head

traversal(head)