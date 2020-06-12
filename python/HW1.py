class Account_manage:
    def __init__(self, num, name, save):
        self.account_num = num
        self.account_name = name
        self.account_save = save
        self.payment_detail = []
        print("결과: 계좌가 생성되었습니다.")
        
    def saving(self, save):
        self.account_save += save
        print("결과: 예금이 성공되었습니다.")
        self.payment_detail.append(("입금", save))

    def withdraw(self, get):
        self.account_save -= get
        print("결과: 출금이 성공되었습니다.")
        self.payment_detail.append(("출금", get))

    def transfer(self, reciever, send):
        self.account_save -= send
        print("결과: 송금이 성공되었습니다.")
        self.payment_detail.append(("송금", reciever, send))

    def recieve(self, sender, get):
        self.account_save += get
        self.payment_detail.append(("입금", sender, send))




def menu():
    print("""
------------------------------------------------------------------------------

1.계좌생성 | 2.계좌목록 | 3.예금 | 4.출금 | 5.송금 | 6.내역조회 | 7. 종료

------------------------------------------------------------------------------
""")

account = []

while True:
    menu()
    print("선택> ", end = "")
    choose = int(input())
    if choose == 1:
        print("""
-------------
계좌생성
-------------
""")
        print("계좌번호: ", end ="")
        num = input()
        print("계좌주: ", end = "")
        name = input()
        print("초기입금금액: ", end = "")
        save = int(input())
        new = Account_manage(num, name, save)
        account.append(new)

    elif choose == 2:
        print("""
-------------
계좌목록
-------------
""")
        for i in account:
            print(f"{i.account_num}   {i.account_name}   {i.account_save}")

        print("----------------------------------------------------")

    elif choose == 3:
        print("""
-------------
예금
-------------
""")
        print("계좌번호: ", end = "")
        num = input()
        print("예금액: ", end = "")
        save = int(input())

        for i in account:
            if i.account_num == num:
                i.saving(save)
    
    elif choose == 4:
        print("""
-------------
출금
-------------
""")
        print("계좌번호: ", end = "")
        num = input()
        print("출금액: ", end = "")
        get = int(input())

        for i in account:
            if i.account_num == num:
                i.withdraw(get)

    elif choose == 5:
        print("""
-------------
송금
-------------
""")
        print("계좌번호: ", end = "")
        num = input()
        print("입금계좌번호: ", end = "")
        num_recieve = input()
        print("이체금액: ", end = "")
        send = int(input())

        for i in account:
            if i.account_num == num:
                i.transfer(num_recieve, send)

        for j in account:
            if j.account_num == num_recieve:
                j.recieve(num, send)


    elif choose == 6:
        print("""
-------------
내역 조회
-------------
""")
        print("계좌번호: ", end = "")
        num = input()

        for i in account:
            if i.account_num == num:
                for list in i.payment_detail:
                    print(f"{list}")

    elif choose == 7:
        print("프로그램 종료")
        break

    else:
        print("ERROR")
                
