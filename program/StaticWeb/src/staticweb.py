import threading
import socket
from sys import argv


class StaticWebServer(object):
    def __init__(self, port=8080):
        self.port = port
        tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        tcp_server_socket.bind(('', self.port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        while True:
            new_socket_out, ip_port = self.tcp_server_socket.accept()
            print(f'Request from {ip_port[0]}:{ip_port[1]}')

            sub_thread = threading.Thread(target=StaticWebServer.show_page, args=(new_socket_out,))
            sub_thread.start()

    @staticmethod
    def show_page(new_socket: socket.socket):
        recv_data = new_socket.recv(4096)

        if len(recv_data) == 0:
            new_socket.close()
            return

        path = recv_data.decode('utf-8').split(' ', 2)[1]

        if path == '/':
            path = '../static/index.html'
        else:
            path = '../static' + path

        response = None

        try:
            file = open(path, 'rb')
        except FileNotFoundError:
            file = open('../static/error.html', 'rb')

            response_line = 'HTTP/1.1 404 Not Found\r\n'
            response_head = 'Server: PSW\r\n'

            response_body = file.read()

            response = response_line + response_head + '\r\n'
            response = response.encode('utf-8') + response_body
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_head = 'Server: PSW\r\n'

            response_body = file.read()

            response = response_line + response_head + '\r\n'
            response = response.encode('utf-8') + response_body
        finally:
            new_socket.send(response)

        new_socket.close()


if __name__ == '__main__':
    if len(argv) == 1:
        static_web_Server = StaticWebServer()
        static_web_Server.start()
    elif len(argv) == 2:
        if argv[1].isdigit():
            static_web_Server = StaticWebServer(int(argv[1]))
            static_web_Server.start()
