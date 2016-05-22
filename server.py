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
        self.socket.connect(("gmail.com", 80))
        self.host = self.socket.getsockname()[0]

    def send_message(self):
        # Отправить сообщение
        pass

    def check_messages(self):
        # Проверить сообщения от клиента
        pass

    def loop(self):
        # Петелька
        pass

