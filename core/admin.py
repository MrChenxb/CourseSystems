# coding:utf-8

"""管理员视图"""
from interface import admin_interface
from interface import common_interface
from lib import common
admin_info = {
    'user': None
}

# 1.管理员注册
def register():
    while True:
        username = input('请输入用户名==>').strip()
        password = input('请输入密码==>').strip()
        re_password = input('请再次输入密码==>').strip()

        if username == '' or password == '' or re_password == '':
            print('用户名或密码不能为空！')
            continue

        if password == re_password:
            # 调用接口层，管理员注册接口
            flag,msg = admin_interface.admin_register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次输入密码不一致，请重新输入！')

# 2.管理员登录
def login():
    while True:
        username = input('请输入用户名==>').strip()
        password = input('请输入密码==>').strip()

        if username == '' or password == '':
            print('用户名或密码不能为空！')
            continue
        flag,msg = common_interface.login_interface(username,password,user_type='admin')
        if flag:
            print(msg)
            # 记录当前用户状态（可变类型不需要global）
            admin_info['user'] = username
            break
        else:
            print(msg)

# 3，管理员创建学校
@common.auth('admin')
def create_school():
    while True:
        school_name = input('请输入学校名称==>').strip()
        school_addr = input('请输入学校地址==>').strip()

        if school_name == '' or school_addr == '':
            print('学校名称或学校地址不能为空！')
            continue
        flag,msg = admin_interface.create_school_interface(
            # 学校名称，学校地址，创建学校的管理员
            school_name,school_addr,admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)
    pass


# 4.管理员创建课程
@common.auth('admin')
def create_course():
    while True:
        # 1)让管理员先选择学校
        # 1.1) 调用接口，获取所有学校的名称并打印
        flag, schoolList_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(schoolList_or_msg)
            break
        for index,school_name in enumerate(schoolList_or_msg):
            print('学校编号:[%s] 学校名称:%s' %(index,school_name))

        choice = input('请输入学校编号==>').strip()
        if choice == '':
            print('学校编号不能为空！')
            continue
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(schoolList_or_msg)):
            print('请输入正确的学校编号！')
            continue
        school_name = schoolList_or_msg[choice]

        # 2)选择学校后，再输入课程名称
        course_name = input('请输入创建的课程名称==>').strip()
        if course_name == '':
            print('课程名称不能为空！')
            continue
        # 3)最后调用创建课程接口，让管理员去创建课程
        flag, msg = admin_interface.create_course_interface(school_name, course_name, admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5.管理员创建讲师
@common.auth('admin')
def create_teacher():
    while True:
        teacher_name = input('请输入老师的名字==>').strip()
        if teacher_name == '':
            print('老师的名字不能为空！')
            continue

        flag,msg = admin_interface.create_teacher_interface(teacher_name,admin_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)


admin_func = {
    '0': ['退出', None],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['创建学校', create_school],
    '4': ['创建课程', create_course],
    '5': ['创建讲师', create_teacher]
}

def admin_view():
    while True:
        print(' 欢迎来到管理员视图 '.center(30,'='))
        for index,func in admin_func.items():
            print('[%s] %s'%(index,func[0]))
        print(' end '.center(30,'='))

        choice = input('请输入功能编号==>').strip()
        if choice not in admin_func:
            print('请输入正确的功能编号!')
            continue
        if choice == '0':
            break
        admin_func[choice][1]()