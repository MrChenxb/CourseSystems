# coding:utf-8
from db import models
def check_course_interface(teacher_name):
    tea_obj = models.Teacher.select(teacher_name)
    # course_list = tea_obj.course_list_from_tea
    course_list = tea_obj.show_course()
    if course_list:
        return True,course_list
    return False, '老师没有选择课程！'

def add_course_interface(course_name,teacher_name):
    tea_obj = models.Teacher.select(teacher_name)
    course_list = tea_obj.course_list_from_tea
    if course_name in course_list:
        return False,'该课程已添加！'
    tea_obj.add_course(course_name)
    return True,'添加课程成功！'

def get_student_interface(course_name, teacher_name):
    tea_obj = models.Teacher.select(teacher_name)
    student_list = tea_obj.get_student(course_name)

    if not student_list:
        return False,'没有学生选择该课程！'
    return True,student_list

def change_score_interface(course_name,stu_name,
                           score,teacher_name):
    tea_obj = models.Teacher.select(teacher_name)
    tea_obj.change_score(course_name,stu_name,score)
    return True,'修改分数成功！'