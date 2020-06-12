class A:
    n = "A 클래스 동작"
    def __init__(self): #인스턴스 메소드
        A.n = " A 생성자 동작"
        print("생성자 동작")
    def method():
        print("A_method")
    @classmethod
    def M(cls): #클래스 참조 시켜야함 cls는 클래스 자첼를 의미
        cls.n = "data"
        print("클래스 메소드 동작")

    @staticmethod
    def M(): #클래스 참조 시켜야함 cls는 클래스 자첼를 의미
        A.n = "data"
        print("클래스 메소드 동작")

class B:
    b_n="B 클래스 동작"
    def __init__(self):
        B.b_n = "B 생성자 동작"
        super().__init__() #new class method 동작
    def method():
        print("B method")


b = B()
b.method()
