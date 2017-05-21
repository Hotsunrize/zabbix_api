#!/usr/bin/env python
# -*- coding: utf-8 -*-
from core import auth
from core import operation
import time

status_data = {
    'account_id':None,
    'is_authenticated':False,
    'auth_id':None,
    'account_data':None
}


class API:
    get_post_obj = operation.return_post()
    action_obj = operation.Action()
    def __init__(self):
        pass
    def Acc_info(self):
        print(status_data['account_data'])
    def Add_host(self):
        start_time = time.time()
        res = self.action_obj.create(self.get_post_obj.get_create_post(status_data['auth_id']))
        print("执行时间:%ss" %(time.time() - start_time))
        err_info = res[0]
        suc_num = len(res[1])
        fal_num = len(res[0])
        for i in err_info:
          print("\033[31;1m添加失败:\t%s\033[0m" %i)
        print("\033[32;1m成功添加主机:\t%s\033[0m" %suc_num)
       # print("\033[31;1m失败:%s\033[0m" %fal_num)
    def Get_info(self):
        res = self.action_obj.get_info(self.get_post_obj.get_info_post(status_data['auth_id']))
        print(res)
    def Log_out(self):
        exit()
    def interactive(self,acc_data):
        '''
        interact with user
        :return:
        '''
        menu = u'''
        ------- zabbix_api ---------
        \033[32;1m1.  用户信息
        2.  批量添加(功能已实现)
        3.  查询信息(功能已实现)
        4.  退出
        \033[0m'''
        menu_dic = {
            '1': self.Acc_info,
            '2': self.Add_host,
            '3': self.Get_info,
            '4': self.Log_out,
        }
        exit_flag = False
        while not exit_flag:
            print(menu)
            user_option = raw_input(">>:").strip()
            if user_option in menu_dic:
                menu_dic[user_option]()

            else:
                print("\033[31;1m选项不存在!\033[0m")
    def run(self):
        '''
        this function will be called right a way when the program started, here handles the user interaction stuff
        :return:
        '''
        acc_data = auth.acc_login(status_data)
        if status_data['is_authenticated']:
            status_data['account_data'] = acc_data
            self.interactive(status_data)
