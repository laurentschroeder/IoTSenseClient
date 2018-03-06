# -*- coding: utf-8 -*-
import socket
import iot_parser
import iot_json_parser
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.178.76', 2000))
print('Connection established\n')
localtime = time.asctime(time.localtime(time.time()))
#time_string = input('Geben Sie das Datum im Format yyyy-mm-dd-hh-mm an:\n')
s.sendall('set time '.encode() + localtime.encode('utf-8') + '\r\n'.encode())
s.close()

passive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
passive_socket.bind((socket.gethostname(), 2000))
passive_socket.listen(1)
active_socket, client_address = passive_socket.accept()
print('Got connection from', client_address)

while True:

    while True:
        new_data = active_socket.recv(256)
        if not new_data:
            break
        else:
            iot_json_parser.parse_json(new_data)
    active_socket.close()
    print("Socket closed.")
    break
