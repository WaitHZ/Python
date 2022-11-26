"""
    Define the server class and provide the following methods:
    1. run()  The method to run in the main module.
    2. set_candidate()  Set voting objects.
    3. set_vote_time() Specify a voting time.
    4. Plot the statistical results as a bar graph.
"""


import threading
import time

import matplotlib.pyplot as plt

from . import comsocket
from . import waitsocket


class Server(object):
    def __init__(self):
        self.candidate_list = []
        self.score_list = []
        self.time = 0

    def run(self):
        print('Welcome to Console Vote Server!\n')

        self.set_candidate()
        print()
        self.set_vote_time()
        print()

        cho = input("Type 1 to start voting, and others to exit:")

        if cho == '1':
            start_time = time.time()

            wait_socket = waitsocket.WaitSocket()
            wait_socket.set_port_reuse()
            wait_socket.bind(9090)  # You can change this default port.
            wait_socket.listen(128)

            while True:
                if time.time() - start_time >= self.time * 60:
                    print('Deadline for voting')
                    break

                com_dict = wait_socket.accept()

                com_socket = comsocket.ComSocket(com_dict['socket'])

                sub_thread = threading.Thread(target=comsocket.ComSocket.communicate, args=(com_socket, self))
                sub_thread.daemon = True

                sub_thread.start()

            self.draw_bar()

        else:
            print('Thanks for choosing')

    def set_candidate(self):
        num = int(input('Enter the number of candidates:'))

        for i in range(num):
            name = input(f'Enter {i+1}th candidate name:')
            self.candidate_list.append(name)
            self.score_list.append(0)

    def set_vote_time(self):
        self.time = float(input('Enter voting time (minutes):'))

    def draw_bar(self):
        fig, ax = plt.subplots()

        colors = ['r', 'b', 'g', 'y']
        bar_colors = [colors[i % len(colors)] for i in range(len(self.candidate_list))]

        ax.bar(self.candidate_list, self.score_list, color=bar_colors)

        ax.set_ylabel('score')
        ax.set_ylim(0, max(self.score_list)+2)
        ax.set_title('Voting results')

        plt.savefig('./res_fig/VotingResult.png')
