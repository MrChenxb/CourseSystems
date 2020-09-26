# coding:utf-8
from db import models

def student_register_interface(username,password):
    student_obj = models.Student.select(username)
    if student_obj:
        return False,f'学生用户[{username}]已存在！'
    student_obj = models.Student(username,password)
    student_obj.save()
    return True,f'学生用户[{username}]创建成功！'

# 学生登录接口
"""
def student_login_interface(username,password):
    student_obj = models.Student.select(username)
    if student_obj:
        if password == student_obj.pwd:
            return True,f'学生用户[{username}]登录成功！'
        return False,f'密码错误！'
    return False,f'学生用户[{username}]不存在！'
"""

# 学生选择学校接口
def choice_school_interface(school_name,student_name):
    # 1.判断当前学生是否存在学校
    stu_obj = models.Student.select(student_name)
    if stu_obj.school:
        return False,f'当前用户已选择过学校了！'
    # 2.若不存在，则调用学生对象中选择学校的方法
    stu_obj.choice_school(school_name)
    return True,'选择学校成功！'

def get_course_list_interface(student_name):
    stu_obj = models.Student.select(student_name)
    school_name = stu_obj.school
    if not school_name:
        return False,'没有学校，请先选择学校！'

    school_obj = models.School.select(school_name)
    if not school_obj.course_list:
        return False,'没有课程，请先联系管理员！'
    return True,school_obj.course_list

def add_course_interface(course_name,stu_name):
    stu_obj = models.Student.select(stu_name)
    if course_name in stu_obj.course_list:
        return False,'该课程已经选择过了！'
    stu_obj.add_course(course_name)
    return True,f'[{course_name}]课程添加成功!'

def check_score_interface(stu_name):
    stu_obj = models.Student.select(stu_name)
    if stu_obj.score_dict:
        return stu_obj.score_dict