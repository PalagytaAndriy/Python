import requests

import socket
import threading

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.bind((HOST, PORT))
sock.listen()
api_url = f'https://api.openweathermap.org/data/2.5/weather'
appid = 'bf7329866498355636bce98b67774b95'


def weather(client, ):
    while True:
        try:
            client.send('Виконано'.encode('utf-8'))
            city = client.recv(1024).decode('utf-8')
            r = requests.get(url=api_url, params=dict(APPID=appid, q=city.title(), units='metric'))
            res = r.json()
            answer = f'Місто: - {res["name"]}\n' \
                      f'Температура: {round(res["main"]["temp"])}\n' \
                      f'Відчувається температура: {round(res["main"]["feels_like"])}\n' \
                      f'Погода: {res["weather"][0]["description"]}\n' \
                      f'Швидкість вітру: {round(res["wind"]["speed"])} м\с\n'
            client.send(answer.encode('utf-8'))

        except:
            client.close()
            break

def receive():
    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=weather, args=(conn, ))
        thread.start()


receive()