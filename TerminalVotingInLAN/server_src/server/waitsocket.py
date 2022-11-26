"""
    Define the socket class used by the server to wait for client_src connections, and provide the following methods:

    1.set_port_reuse()
    Set port multiplexing

    2.bind(port)
    Bind port

    3.listen(max_wait_client)
    Listen port

    4.accept()
    Wait for the client_src to connect, when the connection occurs, return a dictionary (including new socket, ip, port)
"""

import socket


class WaitSocket(object):
    def __init__(self):
        self.wait_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    def set_port_reuse(self):
        self.wait_socket.setsockopt(socket. SOL_SOCKET, socket. SO_REUSEADDR, True)

    def bind(self, port):
        self.wait_socket.bind(('', port))

    def listen(self, max_wait_client):
        self.wait_socket.listen(max_wait_client)

    def accept(self):
        new_socket, ip_info = self.wait_socket.accept()

        return {'socket': new_socket, 'ip': ip_info[0], 'port': ip_info[1]}
