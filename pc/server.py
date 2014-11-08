# /usr/local/bin/python3
import socket
import os

SHUTDOWN = 0x01
HALT = 0x02
REBOOT = 0x03

def shutdown():
	if 'nt' == os.name:
		return os.system('shutdown /s /t 0')
	elif 'posix' == os.name:
		return os.system('shutdown -P +0')

def halt():
	if 'nt' == os.name:
		return os.system('shutdown ')
	elif 'posix' == os.name:
		return os.system('shutdown -H +0')

def reboot():
	if 'nt' == os.name:
		return os.system('shutdown')
	elif 'posix' == os.name:
		return os.system('shutdown -r')
HOST = ''
PORT = 50007
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

def recvcmd():
	command, addr = server.recvfrom(1024)
	print(command[0], SHUTDOWN)
	ret = 1000
	if command[0] == SHUTDOWN:
		ret = shutdown()
	print(ret)
	return ret
stat = 1000
while stat is not 0:
	stat = recvcmd()
ret = int.to_bytes(stat, 1, 'big', signed=True)
server.sendto(ret, addr)
