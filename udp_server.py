"""
File Name: udp_server.py
Author: Rahim Siddiq
Date: 08/30/2024
CST311 Programming Assignment 1
Description: UDP server script - listens on a specified ip and port. The server receives a message
    from a client, converts it to uppercase and returned the modified message back to the client.
"""

import socket

HOST = "10.0.0.1"  # todo: specify the correct hostname of IP address to communicate with the server.
PORT = 12345  # todo: specify the correct port number to communicate with the server.

# open a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('Server listening on {}:{}'.format(HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        s.sendto(data.upper(), addr)