# !/usr/bin/python
# -*- coding: utf-8 -*-

u"""
Астра - пульт для запуска, воспроизведения и управления воспроизведением
видо-файлов с компьютера...
"""
import asyncore
import os
from server import Server


class Manager(object):
    u"""
    Класс для управления воспроизведением
    1. Запуск и остановка воспроизведения
    2. Мониторинг воспроизведения
    3. Предоставление инфы об имеющихся файлах
    """

    folder = '/home/nesterov/My_projects/astra/test'

    def get_files_list(self):
        u"""Вернуть список имеющихся файлов"""
        return os.listdir(self.folder)

    def run_video(self, file_path):
        u""" Запустить проигрывание"""
        pass

    def pause(self):
        u""" Поставить видео на паузу """
        pass


class AstraApp(object):
    u"""Базовый класс приложения"""

    def run(self):
        u"""Запуск приложения"""

        server = Server(Manager())
        print 'Для подключения введите код: %s' % '-'.join(server.ip.split('.')[2:])

        asyncore.loop()
        # 1. Запустить сокет и показать на экране код подключения
        #
        # 2. Отправить клиенту список медиа-файлов
        #
        # 3. Получив имя файла запустить проигрывание и начать отслеживание
        # процесса проигрывания и реакцию на команды клиента
        #
        # 4. Завершить воспроизведение и отчитаться об этом клиенту


if __name__ == '__main__':
    app = AstraApp()
    app.run()
