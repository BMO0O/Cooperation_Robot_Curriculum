class LinearProbing:
   def __init__(self,size):    
      self.M = size           
      self.a = [None]*size    
      self.d = [None]*size    
                    
   def hash(self,key):      
      return key%self.M

   def put(self,key,data):
      initial_position = self.hash(key)
      i = initial_position
      j = 0 

      while True:
         if self.a[i] == None:
            self.a[i] = key
            self.d[i] = data
            return

         if self.a[i] == key :  
            self.d[i] = data
            return
         j+=1
         i = (initial_position +j)%self.M
         if i == initial_position:
            break
   def get(self,key): 
      initial_position = self.hash(key)
      i = initial_position
      j = 1
      while self.a[i]!=None:
         if self.a[i] == key:
            return self.d[i]
         i = (initial_position + j) % self.M #인덱스 길이보다 더 큰 수가 들어오면 선형적으로 처음으로 돌아가도록 할 수 있게 하기 위해 %를 사용
         j+=1
         if i == initial_position:
            return None
        
      return None
    
    
   def print_table(self): 
      print('\n')
      for i in range(self.M):
         print(f'{i}', " ", end="")
      print('\n')
        
      for i in range(self.M):
         print(f'{self.a[i]}', " ", end="")
      print('\n')
        
      pass
lb = LinearProbing(10)
lb.put(1,'apple')
lb.put(2,'grape')
lb.put(11,'pear')

lb.put(4,'banana')
lb.put(5,'lemon')
lb.put(6,'orange')
lb.put(7,'olive')
lb.put(8,'wter')
lb.put(9,'idk')


lb.put(21,'ttt')
lb.put(33,'ttt')

lb.print_table()

print(lb.get(1))
print(lb.get(11))
