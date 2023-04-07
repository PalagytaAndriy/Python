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


def get_weather(client, ):
    while True:
        try:
            client.send('CITY'.encode('utf-8'))
            city = client.recv(1024).decode('utf-8')
            r = requests.get(url=api_url, params=dict(APPID=appid, q=city.title(), units='metric'))
            res = r.json()
            answer = f'City: {res["sys"]["country"]}, {res["name"]}\n' \
                      f'Temperature: {round(res["main"]["temp"])}\n' \
                      f'Feel likes: {round(res["main"]["feels_like"])}\n' \
                      f'Weather: {res["weather"][0]["main"]} - {res["weather"][0]["description"]}\n' \
                      f'Wind: {round(res["wind"]["speed"])} m\s\n'
            client.send(answer.encode('utf-8'))

        except:
            client.close()
            break

def receive():
    while True:
        conn, addr = sock.accept()
        print(f"Connect with {str(addr)}")
        # conn.send('You connected to server!'.encode('utf-8'))
        thread = threading.Thread(target=get_weather, args=(conn, ))
        thread.start()


receive()