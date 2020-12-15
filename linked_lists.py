class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def push(head, data):
    # create the node and connect to the next point
    # easy to create linked list when data is reversed
    # 8 <- 7 <- 6
    ''' Create node 8 and return it
        create node 7 and next is 8 return 7
        create node 6 and next is 7 return 6'''
    new = Node(data)
    new.next = head # previous which is actually the next 
    return new

head = None
lst = [1,2, 3]
lst.reverse()

# create the linked list 
for x in lst:
    head = push(head, x) 


def do_it(head = None):
    first = []
    second = []
    while head != None:
        try:
        
            first.append(head)
            second.append(head.next)
            head = head.next.next
        except NoneType:
            break
        print('here')
        
    return first, second

        
f, s = do_it(head)
print(f.data, f.next.data, s.data, s.next.data)
