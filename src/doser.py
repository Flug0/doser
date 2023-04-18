import socket

IP = "XX.XXX.XX.XXX"
PORT = 12345

msg = bytes([0]*200)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    sock.sendto(msg, (IP, PORT))