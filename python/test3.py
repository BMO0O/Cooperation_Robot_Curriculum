class A:
    n = 0
    __x = 0
    def __init__(self):
        self.m = 0
        self.__y = 0
    def __method(self):
        print("메소드 사용 ") #이것들은 인스턴스를 부여해주어야만 존재
    def get(self):
        return self.__y
    def get_M(self):
        self.__method()
    
a = A()
a.method()
a.n
a.m
a.get()
#a.x 두개는 사용 불가 
#a.y
"""
두개는 사용 불가, 이것들은 클래스 요소 내에서만 접근 가능
y는 인스턴스 value
"""
