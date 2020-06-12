class Node:
    def __init__(self,key,value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BST:
    def __init__(self): 
        self.root = None
    
    
    def get(self,k): 
        result = self.get_item(self.root,k)
    
        return result
    
    def get_item(self,n,k):
        
        if n== None:
            return 
            
        if n.key > k:
            value = self.get_item(n.left,k)
    
        if n.key < k:
            value = self.get_item(n.right,k)
            
            
        if n.key == k:
            return n.value
            
        return value
        
    
    def put(self, key, value): 
        self.root = self.put_item(self.root,key,value)
        

    def put_item(self,n,key, value):
        
        if n == None:
            n = Node(key,value,left=None,right=None)
        
        elif n.key > key:
            n.left = self.put_item(n.left,key,value)
            
        elif n.key < key:
            n.right = self.put_item(n.right,key,value)
        
        elif n.key == key:
            n.value = value
            
        return n 

 
    def minn(self): 

        if self.root == None:
            return None
        
        return self.minimum(self.root)
    
    def minimum(self,n):
        if n.left == None:
            return n
        return self.minimum(n.left)


    def delete_min(self): 
        if self.root == None:
            return None
        
        self.root = self.del_min(self.root)
        
    
    def del_min(self, n):
        if n.left == None:
            return n.right
        else:
            n.left = self.del_min(n.left)
        
        return n

        

    def delete(self,k): 
        self.root = self.del_node(self.root,k)
    
    def del_node(self,n,k):

        if n == None:
            return None

        if n.key == k:
        
            if n.left == None:
                return n.right
            if n.right == None:
                return n.left
            
            target = n
            n = self.minimum(target.right) #
            n.right =  self.del_min(target.right)
            n.left = target.left            

        elif n.key > k:
            n.left = self.del_node(n.left,k)
            
        elif n.key < k:
            n.right = self.del_node(n.right,k)
        
        
        return n
        

    def pre_order(self,n):
        
        if n == None:
            return
        
        print(n.key," ", end="")
        self.pre_order(n.left)
        self.pre_order(n.right)

    def inorder(self,n):
        
        if n == None:
            return
        self.inorder(n.left)
        print(n.key," ",end="")
        self.inorder(n.right)


bts = BST()
bts.put(500,'apple')
bts.put(600,'banana')
bts.put(200,'melon')
bts.put(100,'orange')
bts.put(400,'lime')
bts.put(250,'kiwi')
bts.put(150,'grape')
bts.put(800,'peach')
bts.put(700,'cherry')
bts.put(50,'pear')

bts.put(350,'lemon')
bts.put(10,'plum')

print('전위순회 \t',"", end="")
bts.pre_order(bts.root)
print(' ')
print('중위순회 \t',"", end="")
bts.inorder(bts.root)


result = bts.get(400)
print('\n', '탐색연산  key: 400, result: ', result)  

result2 = bts.minn()
print('\n 최솟값: ', result2.key)

bts.delete_min()
print('\n 최솟값 삭제연산 ', end ="")
bts.inorder(bts.root)

bts.delete(200)
print('\n삭제 연산 1 : ', end ="")
bts.inorder(bts.root)

bts.delete(700)
print('\n삭제 연산 2 : ', end ="")
bts.inorder(bts.root)

bts.delete(50)
print('\n삭제 연산 3 : ', end ="")
bts.inorder(bts.root)
