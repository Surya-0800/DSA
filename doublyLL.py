class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

head = Node(10)
temp1 = Node(20)
temp2 = Node(30)

head.next = temp1
temp1.prev = head
temp1.next = temp2
temp2.prev = temp1

def insert_at_beg(head,x):
    temp = Node(x)
    head.prev = temp
    temp.next = head

    return temp

def insert_at_end(head,x):
    curr = head
    temp = Node(x)
    while curr.next != None:
        curr =curr.next
    temp.prev = curr
    curr.next = temp

    return head

def del_at_beg(head):
    curr = head.next
    curr.prev = None

    return curr

def del_at_end(head):
    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

def reverse_list(head):
    curr = head
    while curr != None:
        prev = curr
        curr.next,curr.prev = curr.prev,curr.next
        curr = curr.prev

    return prev 

def insert_mid(head,pos,y):
    count = 0
    curr = head
    temp = Node(y)
    for i in range(pos-2):
        curr = curr.next

    temp.next = curr.next
    temp.prev = curr.prev
    curr.next = temp
    curr.next.prev = temp

    return head
    


# insert_at_end(head,40)
def print_list(head):
    curr = head
    while curr != None:
        print('-------')
        print(curr.data)
        curr = curr.next


head = insert_mid(head,3,25)
print_list(head)