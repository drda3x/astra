# !/usr/bin/python
# -*- coding: utf-8 -*-

import json
import socket


def connect(url):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(url)
    s.send(json.dumps({
        'type': 'pause'

    }))

    while True:
        data = s.recv(1024)
        if data:
            print data
        else:
            break

    print 'connection closed'


if __name__ == '__main__':
    connect(('192.168.18.116', 9000))