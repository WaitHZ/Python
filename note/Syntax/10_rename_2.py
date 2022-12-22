import os

os.chdir('./test/')

flag = True

if flag == True:
    file_list = os.listdir()
    
    for i in file_list:
        if i[0] != '.':
            new_name = 'Py_' + i
            os.rename(i, new_name)
        
else:
    file_list = os.listdir()
    
    for i in file_list:
        if i[0] != '.':
            new_name = i[len('Py_'):]
            os.rename(i, new_name)