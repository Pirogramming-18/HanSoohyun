#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1() :
    student_list.append([name,int(score1),int(score2)])

##############  menu 2
def Menu2() :
    for info in student_list:
        if len(info) ==3:
            avg= (info[1]+info[2])/2
            if avg >=90:
                info.append('A')
            elif avg >=80:
                info.append('B')
            elif avg >=70:
                info.append('C')
            else:
                info.append('D')
        


##############  menu 3
def Menu3() :
    print('--------------------------')
    print('name  mid  final  grade')
    print('--------------------------')
    for n in student_list:
        print(n[0]),
        print(n[1]),
        print(n[2]),
        print(n[3])

##############  menu 4
def Menu4():
    for qwe, info in enumerate(student_list):
        if delete in info:
            del student_list[qwe] 

#학생 정보를 저장할 변수 초기화
student_list= []
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        # flag=0
        try:
            name, score1, score2= input('Enter name mid-score final-score : ').split()
        except ValueError:
            print('Num of data is not 3!')
        else:
        
            for n in student_list:
                if name in n:
                    print('Already exist name!')
                    # flag+=1
                    break
            try:
                int(score1)
                int(score2)
            except ValueError:
                print('Score is not positive integer!')
            else:
                Menu1(name, mid, final)
                
        
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :
        if len(student_list)==0:
            print('No student data!')
        else:
            print('Grading to all students.')
            Menu2()
        
        
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        if len(student_list)==0:
            print('No student data!')
        else:
            for n in student_list:
                if len(n) !=4:
                    print("There is a student who didn't get grade")
                    break
            else:
                Menu3()
        
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        if len(student_list) ==0:
            print('No student data!')
        else:
            delete=input('Enter the name to delete : ')
            for n in student_list:
                if delete in n:
                    Menu4(delete)
                    print(delete, 'student information is deleted')
                    break
                else:
                    print('Not exist name!')
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print('Exit Program!')
        break
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print('Wrong number. Choose again')
        #"Wrong number. Choose again." 출력