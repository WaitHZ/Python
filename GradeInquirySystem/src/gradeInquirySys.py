from course import *
from os import system


class GradeInquirySys(object):
    def __init__(self):
        self.course_list = []

    def run(self):
        self.load_course_list()

        while True:
            self.show_menu()

            func_num = int(input('输入选择的功能序号:'))

            if func_num == 0:
                self.save_course_list()
                break
            elif func_num == 1:
                self.print_info()
            elif func_num == 2:
                name = input('课程名称:')
                term = input('修读学期：')
                credit = float(input('课程学分：'))
                grade = int(input('课程得分：'))
                is_major = True if int(input('是否必修（0不是，1是）：')) == 1 else False
                is_honor = True if int(input('是否为荣誉课程（0不是，1是）：')) == 1 else False
                self.add_course(name, term, credit, grade, is_major, is_honor)
            elif func_num == 3:
                name = input('修改课程名称:')
                term = input('修读学期：')
                credit = float(input('课程学分：'))
                grade = int(input('课程得分：'))
                is_major = True if int(input('是否必修（0不是，1是）：')) == 1 else False
                is_honor = True if int(input('是否为荣誉课程（0不是，1是）：')) == 1 else False
                self.amend(name, term, credit, grade, is_major, is_honor)
            elif func_num == 4:
                name = input('查询课程名称:')
                self.search(name)
            elif func_num == 5:
                name = input('删除课程名称：')
                self.search(name)
            elif func_num == 6:
                self.print_all()
            elif func_num == 7:
                term = input('查看学期：')
                self.print_certain_term(term)
            elif func_num == 8:
                self.print_major()
            elif func_num == 9:
                self.save_course_list()

            input()
            system("cls")

    def load_course_list(self):
        data_file = open('course.data', "a+")
        data_file.seek(0, 0)
        tmp_str = data_file.read()
        if tmp_str != '':
            tmp_list = eval(tmp_str)
        else:
            tmp_list = []

        for tmp_dict in tmp_list:
            course = Course(tmp_dict['name'], tmp_dict['term'], tmp_dict['credit'],
                            tmp_dict['score'], tmp_dict['isMajor'], tmp_dict['isHonor'])
            self.course_list.append(course)
        data_file.close()

    def save_course_list(self):
        data_file = open('course.data', "w")
        tmp_list = str([i.__dict__ for i in self.course_list])
        data_file.write(tmp_list)
        data_file.close()

    @staticmethod
    def show_menu():
        print('成绩查询系统')
        print('--------------------------------------')
        print('1.显示成绩详细信息')
        print('2.添加课程信息')
        print('3.修改课程信息')
        print('4.查询课程信息')
        print('5.删除课程')
        print('6.显示所有课程信息')
        print('7.查看指定学期课程和成绩信息')
        print('8.主干成绩查询')
        print('9.保存更改')
        print('0.保存更改并退出系统')
        print('--------------------------------------')

    def add_course(self, name, term, credit, score, is_major, is_honor):
        tmp = Course(name, term, credit, score, is_major, is_honor)
        self.course_list.append(tmp)

    def print_info(self):
        total_score = major_score = honor_score = 0
        total_count = major_count = honor_count = 0
        total_gp = major_gp = honor_gp = 0
        total_credit = major_credit = honor_credit = 0
        for tmp in self.course_list:
            total_score += tmp.score * tmp.credit
            total_count += 1
            total_gp += tmp.GP * tmp.credit
            total_credit += tmp.credit
            if tmp.isMajor:
                major_score += tmp.score * tmp.credit
                major_count += 1
                major_gp += tmp.GP * tmp.credit
                major_credit += tmp.credit
            if tmp.isHonor:
                honor_score += tmp.score * tmp.credit
                honor_count += 1
                honor_gp += tmp.GP * tmp.credit
                honor_credit += tmp.credit

        if total_count != 0:
            print(f"共修读{total_count}门课程，累计学分为{total_credit}, 平均绩点为{total_gp / total_credit:.2f}")
        else:
            print("尚未修读任何课程")
            return
        if major_count != 0:
            print(f"共修读{major_count}门主干课程，累计学分为{major_credit}, 平均绩点为{major_gp / major_credit:.2f}")
        else:
            print("尚未修读任何主干课程")
        if honor_count != 0:
            print(f"共修读{honor_count}门荣誉课程，累计学分为{honor_credit}, 平均绩点为{honor_gp / honor_credit:.2f}")
        else:
            print("尚未修读任何荣誉课程")

    def amend(self, name, term, credit, grade, is_major, is_honor):
        for ind, tmp in enumerate(self.course_list):
            if tmp.name == name:
                self.course_list[ind] = Course(name, term, credit, grade, is_major, is_honor)
                print('修改成功')
                break
        else:
            print("课程列表中没有这门课程")

    def search(self, name):
        for tmp in self.course_list:
            if tmp.name == name:
                print(f'课程名称：{tmp.name}, 修读学期：{tmp.term}, 课程学分{tmp.credit}, 课程绩点{tmp.GP}')
                break
        else:
            print("课程列表中没有这门课程")

    def del_course(self, name):
        for ind, tmp in enumerate(self.course_list):
            if tmp.name == name:
                self.course_list.pop(ind)
                print("删除成功")
                break
        else:
            print("课程列表中没有这门课程")

    def print_all(self):
        for tmp in self.course_list:
            print(f'课程名称：{tmp.name}, 修读学期：{tmp.term}, 课程学分{tmp.credit}, 课程绩点{tmp.GP}')

    def print_certain_term(self, term):
        for tmp in self.course_list:
            if tmp.term == term:
                print(f'课程名称：{tmp.name}, 修读学期：{tmp.term}, 课程学分{tmp.credit}, 课程绩点{tmp.GP}')

    def print_major(self):
        for tmp in self.course_list:
            if tmp.isMajor:
                print(f'课程名称：{tmp.name}, 修读学期：{tmp.term}, 课程学分{tmp.credit}, 课程绩点{tmp.GP}')
