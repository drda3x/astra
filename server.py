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

        self.socket = socket.socket()
        self.host = '127.0.0.1'
        self.socket.connect(("gmail.com", 80))
        self.host = self.socket.getsockname()
        print self.host
        self.socket.bind(self.host)
        self.socket.listen(1)

        print 'host: ' + ':'.join(map(str, self.host))

        conn, addr = self.socket.accept()

        print addr

    def send_message(self):
        # Отправить сообщение
        pass

    def check_messages(self):
        # Проверить сообщения от клиента
        pass

    def loop(self):
        # Петелька
        pass


s = SocketServer()

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
