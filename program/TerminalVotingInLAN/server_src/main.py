"""
    Console Vote(Server)

    Server:
    Run on any device in the local area network
    All voting records will be showed in res_fig by png file
"""

import server.work as work

if __name__ == '__main__':
    ser = work.Server()

    ser.run()
