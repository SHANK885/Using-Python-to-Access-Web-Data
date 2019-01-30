# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4e.org', 80))
cmd = "GET http://www.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data)<1:
        break
    print(data.decode(), end = '')

mysocket.close()