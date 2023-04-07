import socket
import threading

#country = input('Enter country code: ')
city = input("Введіть місто -> ")

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'Виконано':
                sock.send(f'{city}'.encode('utf-8'))

            else:
                print(message)
                new_city = input("Введіть місто -> ")
                sock.send(f'{new_city}'.encode('utf-8'))
        except:
            print("Error")
            sock.close()
            break


receive_th = threading.Thread(target=receive)
receive_th.start()