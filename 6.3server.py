import socket
import sys
import time
import errno
import math
from multiprocessing import Process

def process_start(s_sock):
    while True:
      s_sock.send(str.encode('\t\t\tOnline Calculator\n\n\t\tChoose an operation (1)Log | (2)Square Root | (3)Exponent\n\t\t\tEnter operation number(1/2/3):'))
      while True:
        data = s_sock.recv(2048)
        data = data.decode('utf-8')
        print(data)
        if not data:
             break
        elif data == '1':
            s_sock.send(str.encode('\t\tEnter a number:')) 
            num = s_sock.recv(2048)
            num = int(num)
            num = str(math.log(num))
            print(num)
            s_sock.send(str.encode('\t\tThe answer is '+ num + '\n\t\tPress ENTER to continue'))

        elif data == '2':
             s_sock.send(str.encode('\t\tEnter a number:'))
             num = s_sock.recv(2048)
             num = int(num)
             num = str(math.sqrt(num))
             print(num)
             s_sock.send(str.encode('\t\tThe answer is '+ num + '\n\t\tPress ENTER to continue'))

        elif data == '3':
             s_sock.send(str.encode('\t\tEnter a number:'))
             num = s_sock.recv(2048)
             num = int(num)
             num = str(math.exp(num))
             print(num)
             s_sock.send(str.encode('\t\tThe answer is '+ num + '\n\t\tPress ENTER to continue.'))
             
        else:
            s_sock.send(str.encode('\t\tError!/nWrong number!\n\n\t\tPress ENTER to continue.'))
        break

        s_socket.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)

    finally:
           s.close()
