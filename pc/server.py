# /usr/local/bin/python3
import socket
import os

SHUTDOWN = 0x01
HALT = 0x02

def shutdown():
	if 'nt' == os.name:
		return os.system('shutdown /s /t 0')
	elif 'posix' == os.name:
		return os.system('shutdown -P +0')

HOST = ''
PORT = 50007
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

command, addr = server.recvfrom(1024)
if command[0] == SHUTDOWN:
	ret = shutdown()
ret = int.to_bytes(ret, 4, 'big', signed=True)
server.sendto(ret, addr)
