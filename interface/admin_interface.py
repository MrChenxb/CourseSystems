# coding:utf-8
from db import models


def admin_register_interface(username,password):
    # 1)判断用户是否存在
    # 调用Admin类中的select方法，由该方法去调用db_handler中的select_data功能获取对象
    admin_obj = models.Admin.select(username)
    # 1.1)存在，不允许注册
    if admin_obj:
        return False,f'用户[{username}]已存在！'

    # 1.2) 不存在，调用类实例化得到对象并保存
    admin_obj = models.Admin(username, password)
    models.Admin.save(admin_obj)
    return True,f'用户[{username}]注册成功！'

# 管理员登录接口
"""
def admin_login_interface(username,password):
    # 1)判断用户是否存在
    admin_obj = models.Admin.select(username)

    # 2) 不存在，则证明用户不存在返回给视图层
    if not admin_obj:
        return False,f'用户名不存在！'

    # 3) 若存在，则校验密码
    if password == admin_obj.pwd:
        return True,f'用户[{username}]登录成功！'
    else:
        return False,f'密码错误！'
"""

def create_school_interface(school_name,school_addr,admin_name):
    # 1.查看当前学校是否已存在
    school_obj = models.School.select(school_name)
    # 2.若学校存在，返回False，告诉用户当前学校已存在
    if school_obj:
        return False,f'[{school_name}]学校已存在！'
    # 3.若不存在，则由当前管理员对象来创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name,school_addr)
    return True,f'学校[{school_name}]创建成功！'


def create_course_interface(school_name, course_name, admin_name):
    # 1.查看这门课程是否存在
    # 1.1 先获取学校对象中的课程列表
    school_obj = models.School.select(school_name)
    # 1.2 判断当前课程是否存在课程列表中
    if course_name in school_obj.course_list:
        return False,f'当前课程[{course_name}]已存在！'
    # 1.2 若课程不存在，由管理员来创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(school_obj,course_name)
    return True,f'[{course_name}]课程创建成功！绑定给[{school_name}]校区'


def create_teacher_interface(teacher_name, admin_name,teacher_password = '123'):
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False,f'教师[{teacher_name}]已存在！'
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name,teacher_password)
    return True,f'教师[{teacher_name}]创建成功！'



