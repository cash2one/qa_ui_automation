# -*- coding:utf-8 -*-
'''
Created on 2017年2月7日

@author: sunying
作用：用于操作配置文件
'''

import os, ConfigParser,sys
sys.path.append('./config')
def get_config(env):
    '''获取配置文件信息'''
#     获取当前文件完整路径
#     print os.path.join( os.path.dirname(__file__))
# 获取本项目路径
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    conf = ConfigParser.ConfigParser()
    conf.read(dir +'/JKB/config/env_data.conf')
    #print dir +'/JKB/config/env_data.conf'
#     获取指定env 的配置信息
    itms = conf.items(env)
# 获取指定环境数据：'homepage_url，username，password
    env_dict = {itms[0][0]:itms[0][1], itms[1][0]:itms[1][1],itms[2][0]:itms[2][1]}
#     print env_dict
    return env_dict
if __name__ == '__main__':
    get_config('jkb_qa')