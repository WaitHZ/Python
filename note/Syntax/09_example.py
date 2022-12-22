from os import system
# 通过列表存储学生信息，其内存储的元素将是字典
stu_port = []
id_port = []

def replace():
    '''依据学号修改学员信息'''

    system('clear')
    stu_id = int(input('请输入要修改的学号:'))
    if stu_id in id_port:
        for index, stu in enumerate(stu_port):
            if stu['id'] == stu_id:
                print('学员信息为：')
                print('学号     姓名       年龄 性别')
                print('{0:08d} {1:10s} {2:2d}   {3:s}'.format(stu['id'], stu['name'], stu['age'], stu['gender']))
                print()
                print('依次输入修改后的姓名、年龄、性别，用空格分割')
                name, age, gender = input().split()
                stu_port[index]['name'] = name
                stu_port[index]['age'] = int(age)
                stu_port[index]['gender'] = gender
    else:
        print('该学号不存在')
    print('-' * 24)
    print('输入回车回到主菜单')
    input()
    Menu()

def delete():
    '''依据学号删除学员'''

    system('clear')
    stu_id = int(input('请输入要删除的学号:'))
    if stu_id in id_port:
        for index, stu in enumerate(stu_port):
            if stu['id'] == stu_id:
                print('学员信息为：')
                print('学号     姓名       年龄 性别')
                print('{0:08d} {1:10s} {2:2d}   {3:s}'.format(stu['id'], stu['name'], stu['age'], stu['gender']))
                del_cho = int(input('是否确认删除（1.确认；0.取消）:'))
                if del_cho == 0:
                    break
                elif del_cho == 1:
                    del stu_port[index]
                    id_port.remove(stu_id)
                    print('成功删除')
                    break
    else:
        print('该学生不存在')
    print('-' * 24)
    print('输入回车回到主菜单')
    input()
    Menu()

def search():
    '''学员搜索'''

    system('clear')
    stu_id = int(input('请输入要搜索的学号:'))
    if stu_id in id_port:
        print('学号     姓名       年龄 性别')
        for stu in stu_port:
            if stu['id'] == stu_id:
                print('{0:08d} {1:10s} {2:2d}   {3:s}'.format(stu['id'], stu['name'], stu['age'], stu['gender']))
                break
    else:
        print('无此学生')
    print('-' * 24)
    print('输入回车回到主菜单')
    input()
    Menu()

def add_new():
    '''加入新学员'''

    system('clear')
    stu_id, stu_name, stu_age, stu_gender = input('依次输入学号、姓名、年龄、性别，用空格间隔\n').split()
    stu_id, stu_age = int(stu_id), int(stu_age)
    if stu_id in id_port:
        print('该学号已存在，无法添加')
    else:
        stu_port.append({'id': stu_id, 'name': stu_name, 'age': stu_age, 'gender': stu_gender})
        id_port.append(stu_id)
        print('成功添加')
    print('-' * 24)
    print('输入回车回到主菜单')
    input()
    Menu()

def stu_Show():
    '''按照id升序，打印所有学生信息'''

    stu_port.sort(key=lambda x: x['id'])
    system('clear')
    print('学号     姓名       年龄 性别')
    for stu in stu_port:
        print('{0:08d} {1:10s} {2:2d}   {3:s}'.format(stu['id'], stu['name'], stu['age'], stu['gender']))
    print(f'共计{len(stu_port)}名学生', end='\n')
    print('-' * 24)
    print('按下回车回到主菜单')
    input()
    Menu()


def Menu():
    '''打印主界面菜单'''

    system('clear')
    print('-' * 24)
    print('欢迎进入学生信息管理系统')
    print('-' * 24, end='\n\n')
    print('1.显示全部学生信息')
    print('2.添加新学员')
    print('3.查询学员')
    print('4.删除学员')
    print('5.修改学员信息')
    print('0.退出系统')

    func_choice = int(input('请输入功能选择：'))

    if func_choice == 0:
        system('clear')
        print('安全退出，再见')
    elif func_choice == 1:
        stu_Show()
    elif func_choice == 2:
        add_new()
    elif func_choice == 3:
        search()
    elif func_choice == 4:
        delete()
    elif func_choice == 5:
        replace()

Menu()