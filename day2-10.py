import random
ans=random.randint(1,10)
time=0

while True:
    guess=int(input("guess number?"))
    if ans>guess:
        print("bigger")
        time+=1
        continue
    elif ans<guess:
        print("smaller")
        time+=1
        continue
    else:
        print("right")
        time+=1
        print(time)
        break
        
        
        

