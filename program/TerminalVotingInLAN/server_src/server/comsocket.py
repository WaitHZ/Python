"""
   The point of this class is to define methods for sub-threads to execute.
"""

import socket


class ComSocket(object):
    def __init__(self, ori_socket):
        self.socket = ori_socket

    def communicate(self, obj):
        socket.socket.send(self.socket, str(len(obj.candidate_list)).encode('utf-8'))

        for plan in obj.candidate_list:
            socket.socket.recv(self.socket, 1024)
            socket.socket.send(self.socket, plan.encode('utf-8'))

        cho = int(socket.socket.recv(self.socket, 1024).decode('utf-8'))

        try:
            obj.score_list[cho] += 1
        except IndexError:
            pass
