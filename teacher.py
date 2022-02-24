import socket,threading,time,os,random
from datetime import datetime

HOST = '127.0.0.1'
PORT = 50055

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

def createfolder(n):
    try:
        os.chdir(n)
    except:
        os.mkdir(n)
        os.chdir(n)

createfolder("prof1")#create folder for teacher
createfolder("test1")#create folder for test 1

students_connection=[]
students_names=[]

def timenow():
    t=datetime.now()
    cur_time=t.strftime("%H:%M:%S")
    return cur_time

def ask_questions():
    with open("questions.txt","a+") as f:
        n=int(input("Enter the number of questions in the test : "))
        print("Enter %d questions"%(n))
        for i in range(1,n+1):
            q=str(i)+''+input("Enter question :")+'\n'
            f.write(q)
    print("\n\nTEST QUESTIONS ARE ADDED\n\n")
            

def Announcement(message):
        for student in students_connection:
            student.send(message)

def SendQuestion(student,num):
    #select a question and send
    q=str()
    with open("questions.txt") as f:
        q=f.readlines()[random.randint(0,len(q))]
        student.send(q.encode('ascii'))
    with open("Questions_assigned.txt",'a+') as f:
        s=students_names[num]+'  '+timenow()+'   '+q
        f.write(s)
    print()

def search_student():
    global l
    

def answer_receive(student):
    while True:
        if(True):
            test_answer = student.recv(1024)
            index=students_connection.index(student)
            s_name=students_names[index]
            with open("Questions_submitted.txt",'a+') as f:
                
                with open("Questions_assigned.txt",'r') as g:
                    for i in g.readlines():
                        if i[0]==s_name:
                            l=i
                            break
                l=l+' '+timenow()
                f.write(l+'\n')
            with open("%s.txt"%(s_name),"w") as f:
                f.write(test_answer.decode('ascii')+'\n')
            index = students_connection.index(student)
            students_connection.remove(student)
            student.close()
            student_name = students_names[index]
            students_names.remove(student_name)
            print(student_name,"left the exam.Number of students remaining ",len(students_names))
            print()
            break
        #except:
            #pass

def receive():
    while True:
        student, address = server.accept()
        print(f"connected with {address}")
        student_name = student.recv(1024).decode('ascii')
        students_names.append(student_name)
        students_connection.append(student)
        print(f"name of the client is {student_name}")
        student.send(f"Connected with test server\n".encode('ascii'))
        print(f"All Students in Exam {students_names}")
        SendQuestion(student,len(students_names)-2)
        print()
        thread = threading.Thread(target=answer_receive, args=(student,))
        thread.start()

print("starting test server")
ask_questions()
receive()
choice=1
while(choice):
    if(choice==1):
        Announcement
