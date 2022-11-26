"""
    Console Vote(Client)

    In order to connect smoothly, it is necessary to know the device IPv4 address from the server.
"""


import client.work as work


if __name__ == '__main__':
    ip = input('Please enter the IP address provided by the server:')

    cli = work.Client(ip)

    cli.run()
