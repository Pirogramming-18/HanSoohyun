num=0;
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
    
for i in range(a):
    num += 1
    if num==31:
        
        flag+=1
        break
    R=f'PlayerA : {num}'
    print(R)

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

for i in range(a):
    num += 1
    if num==31:
        
        flag+=1
        break
    R=f'PlayerB : {num}'
    print(R)
    
   