score_list=[]
num=int(input('people?'))
for i in range(num):
    score=int(input('score?'))
    if score<60:
        score=60
    score_list.append(score)
print(score_list)
        
        
    

