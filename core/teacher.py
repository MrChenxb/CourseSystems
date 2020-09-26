# coding:utf-8
"""
教师视图
"""
from lib import common
from interface import common_interface
from interface import teacher_interface

teacher_info = {
    'user': None
}

# 1.教师登录
def login():
    while True:
        username = input('请输入用户名==>').strip()
        password = input('请输入密码==>').strip()

        flag,msg = common_interface.login_interface(username,password,user_type='teacher')
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)

# 2.教师查看教授课程
@common.auth('teacher')
def check_course():
    flag,course_list = teacher_interface.check_course_interface(teacher_info['user'])
    if flag:
        print(course_list)
    else:
        print(course_list)

# 3.教师选择教授课程
@common.auth('teacher')
def choice_course():
    while True:
        flag,school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index,school_name in enumerate(school_list):
            print(f'学校编号为:[{index}], 学校名称为:[{school_name}]')

        choice = input('请输入选择的学校编号==>').strip()
        if not choice.isdigit():
            print('输入有误！')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('输入有误！')
            continue
        school_name = school_list[choice]

        flag2,course_list = common_interface.get_course_in_school_interface(school_name)
        if not flag2:
            print(course_list)
            break
        for index2,course_name in enumerate(course_list):
            print(f'课程编号为:[{index2}], 课程名称为:[{course_name}]')
        choice2 = input('请输入选择的课程编号==>').strip()
        if not choice2.isdigit():
            print('输入有误！')
            continue
        choice2 = int(choice2)
        if choice2 not in range(len(course_list)):
            print('输入课程编号有误！')
            continue
        course_name = course_list[choice2]

        flag3,msg = teacher_interface.add_course_interface(course_name,teacher_info['user'])
        if flag3:
            print(msg)
            break
        else:
            print(msg)

# 4.教师查看课程下学生
@common.auth('teacher')
def check_stu_from_course():
    while True:
        flag,course_list = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print(course_list)
            break
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
        course_name = course_list[choice]

        flag, student_list = teacher_interface.get_student_interface(course_name, teacher_info['user'])
        if flag:
            print(student_list)
            break
        else:
            print(student_list)
            break
# 5.教师修改学生分数
@common.auth('teacher')
def change_score_from_student():
    """
    # 1.先获取老师下所有的课程并选择
    # 2.获取课程下所有的学生，并选择修改的学生
    # 3.调用修改学生分数接口
    """
    while True:
        flag,course_list = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print(course_list)
            break
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
        course_name = course_list[choice]

        flag2, student_list = teacher_interface.get_student_interface(course_name,teacher_info['user'])
        if not flag2:
            print(student_list)
            break
        for index,stu_name in enumerate(student_list):
            print(f'学生编号为:[{index}], 学校姓名为:[{stu_name}]')
        choice_stu = input('请输入学生编号==>').strip()
        if not choice_stu.isdigit():
            print('输入有误！')
            continue
        choice_stu = int(choice_stu)
        if choice_stu not in range(len(student_list)):
            print('输入学生编号有误！')
            continue
        stu_name = student_list[choice_stu]

        score = input('请输入修改的成绩==>').strip()
        if not score.isdigit():
            print('输入成绩有误！')
            continue
        score = int(score)
        flag3,msg = teacher_interface.change_score_interface(
            course_name, stu_name, score, teacher_info['user']
        )
        if flag3:
            print(msg)
            break

    pass


teacher_func = {
    '0': ['退出', None],
    '1': ['登录', login],
    '2': ['查看教授课程', check_course],
    '3': ['选择教授课程', choice_course],
    '4': ['查看课程下学生', check_stu_from_course],
    '5': ['修改学生分数', change_score_from_student],
}


def teacher_view():
    while True:
        print(' 欢迎来到教师视图 '.center(30,'='))
        for index,func in teacher_func.items():
            print('[%s] %s' %(index,func[0]))
        print(' end '.center(30,'='))

        choice = input('请输入功能编号==>').strip()
        if choice not in teacher_func:
            print('请输入正确的功能编号')
            continue
        if choice == '0':
            break
        teacher_func[choice][1]()