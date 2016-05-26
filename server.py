# !/usr/bin/python
# -*- coding: utf-8 -*-

u"""
Пакет для работы сервера приложения
"""

import json
import socket
import asyncore


class Server(asyncore.dispatcher):
    u"""
    Сервер, запускающийся в отдельном потоке, работающий с клиентом
    """

    class RequestHandler(asyncore.dispatcher_with_send):

        def __init__(self, conn, proc_class):
            self.proc_class = proc_class
            super(Server.RequestHandler, self).__init__(conn)

        def handle_close(self):
            self.close()

        def handle_read(self):
            data = self.recv(1024)
            if data:
                try:
                    data = json.loads(data)
                    getattr(self.proc_class, data['type'])(*data['data'])
                except Exception:
                    pass

    def __init__(self, proc_class=None):

        self.proc_class = proc_class

        # Создать сокет, выделить его в отдельный поток
        # Настроить общение с сокетом
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('gmail.com', 80))
        self.ip = s.getsockname()[0]
        s.close()

        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((self.ip, 9000))
        self.listen(1)

    def handle_accept(self):
        conn, addr = self.accept()
        self.RequestHandler(conn, self.proc_class)


s = Server()
asyncore.loop()
print "I'm here"


   # def send_message(self):
   #    # Отправить сообщение
   #    pass
   #
   # def check_messages(self):
   #     # Проверить сообщения от клиента
   #     pass
   #
   # def loop(self):
   #     # Петелька
   #     pass
s = Server()

# Определить IP

# TCP сервер
# import SocketServer
#
#
# class MyServer(SocketServer.BaseRequestHandler):
#     def handle(self):
#         print self.request.recv(1024).strip()
#
#
# sever = SocketServer.TCPServer((ip, 9000), MyServer)
# sever.serve_forever()

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
