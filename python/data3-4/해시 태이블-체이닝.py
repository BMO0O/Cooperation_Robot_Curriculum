class Chaining:
    class Node:
        def __init__(self,key,data, link): 
            self.key = key
            self.data = data
            self.next = link
        
    def __init__(self, size):
        self.a = [None]*size
        self.size = size
    
    def hash(self,key):
        return key%self.size
 
    def put(self,key,data): 
        i = self.hash(key)
        p = self.a[i]
        
        while p != None:
            if key == p.key:  
                p.data = data
                return 
            p = p.next  
        

        self.a[i] = self.Node(key, data, self.a[i])
        
        
    def get(self,key):
        index = self.hash(key)
        
        this_time_node = self.a[index]

        while this_time_node:
            if this_time_node.key == key:
                return this_time_node.data

            this_time_node = this_time_node.next

        return None

    
    
    def print_table(self): 
        
        for index, first_node in enumerate(self.a):
            print(index," ", end ="")
            
            this_time_node = first_node
            
            while this_time_node:
                print(f"-> [ {this_time_node.key}, {this_time_node.data}] ", end="")
                
                this_time_node = this_time_node.next
        
            print('\n')

t = Chaining(13)
t.put(55,'cherry')
t.put(18,'banana')
t.put(35,'lime')
t.put(22,'mango')
t.put(63,'watermelon')
t.put(50,'orange')
t.put(37,'apple')
             
t.print_table()

result = t.get(50)
print(result)
