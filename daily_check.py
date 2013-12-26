# coding:utf-8

# date: 2013/12/26
# author: heropeng
# version: 1.0.0
# about: it's for check the daily task
"""这是个检查每日学习情况的脚本，预定的是每天学习三项内容，
以一问一答的方式获取学习结果，最后将学习情况保存到文件中。
待加入的功能：1.指定保存文件夹，2.用字典存储，做一个小数据库。"""

import datetime
import os

os.chdir('/Users/heropeng/Documents')
now = datetime.datetime.now()

learning_project = ['English', 'Spanish', 'Programing']
R = []


def add_record(answer):
    '''如果回答是y，则添加学习记录'''
    if answer == 'y':
        R.append(learning_project[i])
    if answer == 'n':
        pass

for i in range(3):
    prompt = 'Have you done your learning of {project}>>>'.format(project=learning_project[i])
    print(prompt)
    answer = input("y or n >>>")
    add_record(answer)

record = '{0} I have learned {1}.\n'.format(now, R)

print(record)
with open('dc_record.txt', 'a') as dc_record:
    dc_record.writelines(record)
