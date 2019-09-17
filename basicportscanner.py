#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = input('Enter the IP you want to scan! \n')
port = int(input('Enter the port you want to scan! \n'))

def Scanner(port):
    if s.connect_ex((IP, port)):
        print("The port is closed!")
    else:
        print("The port is open!")
Scanner(port)
