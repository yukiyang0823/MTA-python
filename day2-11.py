import random
while True:
    inkey=input("按任意建在按enter擲骨子，直接按enter遊戲結束")
    if len(inkey)>0:
        num=random.randint(1,6)
        print("你的點數是:",str(num))
    else:
        print("遊戲結束")
        break

