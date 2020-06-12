class Node:
    def __init__(self,item,link):
        self.item = item
        self.next = link
        
def add(item): # 삽입연산
    global rear
    global front
    global size 
    

    new_node = Node(item, None)
    if size == 0:
        front = new_node
    else:
        rear.next = new_node 
 
    rear = new_node 
    size+=1
    
    
def remove(): # 삭제연산  

    global rear
    global front
    global size     
    
    if size !=0:
        fitem = front.item
        front = front.next
        size -= 1
        if size == 0:
            rear == None
        
        return fitem

def print_q(): # 큐 출력
    
    p = front

    print('front:\t', end="")
    
    while p:
        
        if p.next !=None:
            print(p.item, '-> ', end = "")
        else:
            print(p.item, end ="")
        p = p.next
    print(' :rear')

# 초기화 3개
size = 0
rear = None
front =None

add('apple')
add('orange')
add('cherry')
add('pear')
print('사과, 오렌지, 체리, 배 삽입 후: \t', end='')
print_q()

remove()
print('remove한 후: \t', end="")
print_q()  
remove()
print('remove한 후: \t', end="")
print_q()  

add('grape')
print('포도 삽입 한 후: \t', end="")
print_q()
