# coding:utf-8
"""
用于保存对象与获取对象
"""
import os
import pickle
from conf import settings


def select_data(cls, username):
    class_name = cls.__name__
    user_dir_path = os.path.join(settings.DB_PATH,class_name)

    # 3) 拼接当前用户的文件路径（用户名）
    user_path = os.path.join(user_dir_path, username)

    # 4)打开文件，获取对象
    if os.path.exists(user_path):
        with open(user_path,mode='rb') as f:
            obj = pickle.load(f)
        return obj


def save_data(obj):
    # 1) 获取对象的保存文件夹路径（类名）
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(settings.DB_PATH,class_name)

    # 2)判断文件夹是否存在
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 3) 拼接当前用户的文件路径（用户名）
    user_path = os.path.join(user_dir_path, obj.user)

    # 4)打开文件，保存对象，通过pickle
    with open(user_path,mode='wb') as f:
        pickle.dump(obj,f)