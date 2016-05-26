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
            asyncore.dispatcher_with_send.__init__(self, conn)
            self.proc_class = proc_class

        def handle_close(self):
            self.close()

        def handle_read(self):
            data = self.recv(1024)
            if data:
                try:
                    data = json.loads(data)
                    responce = getattr(self.proc_class, data['type'])(*data['data'])

                    self.send(json.dumps(responce))

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
