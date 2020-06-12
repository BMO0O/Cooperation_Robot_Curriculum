class A:
    n="A 클래스 동작"
    def __init__(self):
        A.n="A생성자 동작"
        print("생성자 동작")
    def method():
        print("A_method")
    @classmethod
    def M(cls):
        cls.n=:"data"
    @staticmethod
    def M():
        A.n=:"data"
    
class B(A):
    b_n="B틀래스 동작"
    def __init__(self):
        B.b_n="B생성자 동작"
        #super().__init__()
    def method():
        print("B_method")


b=B()
print(b.n,b.b_n)
      
