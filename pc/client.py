import socket

HOST = '<broadcast>'
PORT = 50007
SHUTDOWN = 0x01
HALT = 0x02
addr = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
client.sendto(b'\x01', addr) 
