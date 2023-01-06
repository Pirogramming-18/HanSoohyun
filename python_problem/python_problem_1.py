global num
num=0
import random
def nom(X,Y):
        for i in range(a):
            global num
            global flag
            num += 1
            if num==31:
                print(f"{Y} win!")
                flag+=1
                break
            R=f'{X} : {num}'
            print(R)
        

while True:
    global flag
    flag=0
    while (True):
        a=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :")
        try:
            a = int(a)        
        except:
            print("정수를 입력하세요")
            continue
        if (type(a) != int):
            print("정수를 입력하세요")
        elif(a <= 0 or a > 3):
            print("1,2,3 중 하나를 입력하세요")
        else:
            break
    
    nom(X="playerA",Y="computer")
    if flag==1:
        break
        
    a=random.randrange(1,4) 
    nom(X="computer",Y="playerA")
    if flag==1:
        break
    