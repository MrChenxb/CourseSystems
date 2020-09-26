# coding:utf-8
"""
公共方法
"""

# 多用户登录认证装饰器
from functools import wraps
def auth(role):
    """
    多用户登录认证装饰器
    :param role:角色-->管理员、学生、老师
    :return:
    """
    from core import admin,student,teacher
    def login_auth(func):
        @wraps(func)
        def inner(*args,**kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args,**kwargs)
                    return res
                else:
                    print('当前没有管理员用户登录！')
            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args,**kwargs)
                    return res
                else:
                    print('当前没有学生用户登录！')
            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args,**kwargs)
                    return res
                else:
                    print('当前没有教师用户登录！')
            else:
                print('当前视图没有权限！')
        return inner
    return login_auth