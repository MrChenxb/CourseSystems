# coding:utf-8
from core import admin
from core import student
from core import teacher


func_dic = {
    '0': ['退出', None],
    '1': ['管理员功能', admin.admin_view],
    '2': ['学生功能', student.student_view],
    '3': ['老师功能', teacher.teacher_view],
}


def run():
    while True:
        print(' 欢迎来到选课系统 '.center(30,'='))
        for index,func in func_dic.items():
            print('[%s] %s' %(index,func[0]))
        print(' end '.center(30,'='))

        choice = input('请输入功能编号==>').strip()
        if choice not in func_dic:
            print('输入有误，请重新输入')
            continue
        if choice == '0':
            break
        func_dic.get(choice)[1]()