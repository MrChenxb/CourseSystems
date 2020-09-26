# coding:utf-8
"""
公共接口
"""
import os
from conf import settings
from db import models

# 获取所有学校名称接口
def get_all_school_interface():
    # 1) 获取学校文件夹路径
    school_dir = os.path.join(settings.DB_PATH,'School')
    # 2) 判断文件是否存在
    if (not os.path.exists(school_dir)) or os.listdir(school_dir) == []:
        # 2.1) 若不存在，返回False，请联系管理员
        return False,'没有学校，请先联系管理员！'
    # 2.2) 若存在，则获取文件夹中所有文件的名字
    school_list = os.listdir(school_dir)
    return True,school_list

# 公共登录接口
def login_interface(user, pwd, user_type):
    if user == '' or pwd == '':
        return False,f'用户名和密码不能为空!'
    if user_type == 'admin':
        obj = models.Admin.select(user)
    elif user_type == 'student':
        obj = models.Student.select(user)
    elif user_type == 'teacher':
        obj = models.Teacher.select(user)
    else:
        return False,'登录角色不对，请输入角色！'

    if obj:
        if pwd == obj.pwd:
            return True,f'用户[{user}]登录成功！'
        return False,f'密码错误！'
    else:
        return False,f'用户[{user}]不存在！'

def get_course_in_school_interface(school_name):
    school_obj = models.School.select(school_name)
    course_list = school_obj.course_list
    if course_list:
        return True,course_list
    return False,'该学校没有课程！'