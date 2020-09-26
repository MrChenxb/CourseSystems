# coding:utf-8
"""
用于存放类的
学校类、学员类、课程类、讲师类、管理员类
"""
from db import db_handler


class Base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj

    def save(self):
        db_handler.save_data(self)


class Admin(Base):
    # 调用类时触发
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        self.save()

    # 创建学校
    def create_school(self, school_name, school_addr):
        # 该方法内部来调用学校类实例化得到对象，并保存
        school_obj = School(school_name, school_addr)
        school_obj.save()
        pass

    # 创建课程
    def create_course(self, school_obj, course_name):
        # 1. 调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()
        # 2. 获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        # 3. 更新学校数据
        school_obj.save()

    # 创建讲师
    def create_teacher(self,teacher_name,teacher_password):
        teacher_obj = Teacher(teacher_name, teacher_password)
        teacher_obj.save()


# 学校类
class School(Base):
    def __init__(self, name, addr):
        self.user = name
        self.addr = addr
        # 每所学校都有自己的课程列表
        self.course_list = []


class Student(Base):
    def __init__(self,name,pwd):
        self.user = name
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score_dict = {}  # {"course_name": 0}
        # self.payed = {}  # {"course_name": False}

    def choice_school(self,school_name):
        self.school = school_name
        self.save()

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.score_dict[course_name] = 0
        self.save()
        course_obj = Course.select(course_name)
        course_obj.student_list.append(self.user)
        course_obj.save()

class Course(Base):
    def __init__(self, name):
        self.user = name
        self.student_list = []

    pass


class Teacher(Base):
    def __init__(self, name,pwd):
        self.user = name
        self.pwd = pwd
        self.course_list_from_tea = []

    def show_course(self):
        return self.course_list_from_tea

    def add_course(self,course_name):
        self.course_list_from_tea.append(course_name)
        self.save()

    def get_student(self,course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    def change_score(self,course_name,stu_name,score):
        stu_obj = Student.select(stu_name)
        stu_obj.score_dict[course_name] = score
        stu_obj.save()
