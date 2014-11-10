#! /usr/local/bin/python3
import socket
import os

SHUTDOWN = 0x01
SUSPEND  = 0x02
REBOOT   = 0x03
LOGOUT   = 0x04

def shutdown():
	if 'nt' == os.name:
		return os.system('shutdown /s /t 0')
	elif 'posix' == os.name:
		return os.system('shutdown -P +0')

def suspend():
	if 'nt' == os.name:
		return os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
	elif 'posix' == os.name:
		return os.system('pm-suspend')

def reboot():
	if 'nt' == os.name:
		return os.system('shutdown /r /t 0')
	elif 'posix' == os.name:
		return os.system('shutdown -r +0')

def logout():
	if 'nt' == os.name:
		return os.system('shutdown /l')
	elif 'posix' == os.name:
		return os.system('shutdown')
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
	elif SUSPEND == command[0]:
		ret = suspend()
	elif REBOOT == command[0]:
		ret = reboot()
	elif LOGOUT == command[0]:
		ret = logout()
	return ret, addr
stat = 1000
addr = None
while stat is not 0:
	stat, addr = recvcmd()
ret = int.to_bytes(stat, 1, 'big', signed=True)
server.sendto(ret, addr)
