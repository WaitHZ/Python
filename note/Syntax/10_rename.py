import os

file_list = os.listdir()

for i in file_list:
    if i[0] != '.':
        new_name = i[3:]
        os.rename(i, new_name)