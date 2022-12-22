path_name = input('请输入文件路径：').strip()

ind = path_name.rfind('.')

if(ind > 0):
    copy_name = path_name[:ind] + '_copy' + path_name[ind:]

    file_src = open(path_name, 'rb')

    file_new = open(copy_name, 'wb')

    while True:
        con = file_src.read(1024)
        if len(con) == 0:
            break
        file_new.write(con)

    file_src.close()
    file_new.close()
else:
    print('不合法的文件名')
