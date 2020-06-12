class Song: #class에서 앞글자는 대문자로 쓴다
    def __init__(self): #인스턴스 매개변수에서는 무조건 적으로 self가 들어가야 한다/생성자/인스턴스
        self.singer = ""
        self.song_name = ""
        self.num = 0

    def print_all(self): #인스턴스 메서드, self는 필수
        return f"{self.singer},{self.song_name},{self.num}"
        

class M:
    def __init__(self):

    def method1(self):
        print("method1이 실행됩니다.")
        
    def method2(self, x):
        print(x, "method1이 실행됩니다")
