# coding:utf-8
"""
学生视图
"""
from interface import student_interface
from interface import common_interface
from lib import common

student_info = {
    'user': None
}

# 1.学生注册
def register():
    while True:
        username = input('请输入用户名==>').strip()
        password = input('请输入密码==>').strip()
        re_password = input('请再次输入密码==>').strip()

        if username == '' or password == '' or re_password == '':
            print('用户名和密码不能为空！')
            continue
        if password == re_password:
            flag,msg = student_interface.student_register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次输入密码不一致，请重新输入！')

# 2.学生登录
def login():
    while True:
        username = input('请输入用户名==>').strip()
        password = input('请输入密码==>').strip()

        flag,msg = common_interface.login_interface(username,password, user_type = 'student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)
    pass

# 3. 学生选择校区
@common.auth('student')
def choice_school():
    while True:
        # 1.打印所有的学校
        flag,school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index,school_name in enumerate(school_list):
            print(f'学校编号为:[{index}], 学校名称为:[{school_name}]')

        # 2.让用户输入选择学校的编号
        choice = input('请输入选择的学校编号==>').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('输入编号有误！')
            continue
        school_name = school_list[choice]

        # 3.开始调用学生选择学校接口
        flag,msg = student_interface.choice_school_interface(school_name,student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

# 4.学生选择课程
@common.auth('student')
def choice_course():
    while True:
        # 1.先获取当前学生所在学校的列表
        flag,course_list = student_interface.get_course_list_interface(student_info['user'])
        if not flag:
            print(course_list)
            break

        # 2.打印课程列表，并让用户选择课程
        for index,course_name in enumerate(course_list):
            print(f'课程编号为:[{index}], 课程名称为:[{course_name}]')

        choice = input('请输入选择的课程编号==>').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)
        if choice not in range(len(course_list)):
            print('输入课程编号有误！')
            continue
        # 3.获取选择的课程名称
        course_name = course_list[choice]
        flag,msg = student_interface.add_course_interface(course_name,student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)

# 5.学生查看分数
@common.auth('student')
def check_score():
    score_dict = student_interface.check_score_interface(student_info['user'])
    if not score_dict:
        print('没有选择课程！')
    else:
        print(score_dict)

student_func = {
    '0': ['退出', None],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['选择校区', choice_school],
    '4': ['选择课程', choice_course],
    '5': ['查看分数', check_score],
}

def student_view():
    while True:
        print(' 欢迎来到学生视图 '.center(30,'='))
        for index,func in student_func.items():
            print('[%s] %s'%(index,func[0]))
        print(' end '.center(30,'='))

        choice = input('请输入功能编号==>').strip()
        if choice not in student_func:
            print('请输入正确的功能编号！')
            continue
        if choice == '0':
            break
        student_func[choice][1]()