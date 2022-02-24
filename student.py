    import socket,os

HOST = '127.0.0.1'
PORT = 50055


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

name = input("enter your name : ")
client.send(name.encode('ascii'))

q_recved=0

try:
    os.chdir("C://Users//%s//Desktop//practical_exam"%(os.getlogin()))
except:
    os.mkdir("C://Users//%s//Desktop//practical_exam"%(os.getlogin()))
    os.chdir("C://Users//%s//Desktop//practical_exam"%(os.getlogin()))

def receive_question():
    try:
        global question
        question = client.recv(1024).decode('ascii')
        print(question)
        global q_recved
        q_recved=1
        #thread = threading.Thread(target=recevie_message, args=())
    except: 
        print("Can not connect recive the question")
        client.close()


def send_answer():
    message='test answer'
    client.send(message.encode('ascii'))
    print("test closed")
    client.close()
"""
def recevie_annon():
    try:
        message=client.recv(1024).decode('ascii')
        print("\n\n\n\ANNOUNCEMENT : %s \n\n\n\n"%(message))
    except:
        pass

"""
choice=1
while(choice):
    print("\n0.To leave test\n1.Ask for Question\n2.Send Answer\n\nEnter your choice :",end='')
    choice=int(input())
    print()
    if choice==0:
        break
    elif choice==1 and q_recved==0:
        receive_question()
    elif choice==2:
        send_answer()
    elif choice==1 and q_recved==1:
        print("\nQuestion already assigned")
        print(question)
    else:
        print("Invalid choice")
        
