"""
    Define the client class.
"""

import socket


class Client(object):
    def __init__(self, ip):
        self.connect_info = (ip, 9090)
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def run(self):
        self.socket.connect(self.connect_info)

        print('The alternatives are as follows:')

        num = int(self.socket.recv(1024).decode('utf-8'))
        self.socket.send(' '.encode('utf-8'))

        for i in range(num):
            info = self.socket.recv(1024).decode('utf-8')

            print(f'{i}:{info}')

            if i < num - 1:
                self.socket.send(' '.encode('utf-8'))

        cho = input('Enter the serial number of your choice:')

        try:
            self.socket.send(cho.encode('utf-8'))
        except ConnectionResetError:
            print('Voting has ended.')

        print('Thanks for your voting!')
