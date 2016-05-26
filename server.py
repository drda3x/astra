# !/usr/bin/python
# -*- coding: utf-8 -*-

u"""
Пакет для работы сервера приложения
"""

import socket


class SocketServer(object):
    u"""
    Сервер, запускающийся в отдельном потоке, работающий с клиентом
    """

    def __init__(self):

        # Создать сокет, выделить его в отдельный поток
        # Настроить общение с сокетом
        pass


    def send_message(self):
        # Отправить сообщение
        pass

    def check_messages(self):
        # Проверить сообщения от клиента
        pass

    def loop(self):
        # Петелька
        pass


# Определить IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('gmail.com', 80))
ip = s.getsockname()[0]
s.close()

# TCP сервер
import SocketServer


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        print self.request.recv(1024).strip()


sever = SocketServer.TCPServer((ip, 9000), MyServer)
sever.serve_forever()

"""
from threading import Thread
from Queue import Queue
import time

def f(conn):
    print 'call f'
    time.sleep(5)
    conn.put('hello')

q = Queue()
proc = Thread(target=f, args=(q,))
proc.start()
r = None

while not r:
    print 'try to get_data'
    if not q.empty():
        r = q.get()

print r
"""
