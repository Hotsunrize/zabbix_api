#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from core import db_handler
from config import settings
from core import operation
import json
import requests
import getpass


def acc_auth(account,password):
  db_path = db_handler.db_handler(settings.DATABASE)
  account_file = "%s/%s" %(db_path,account)
  print(account_file)
  if os.path.isfile(account_file):
    with open(account_file,'r') as f:
      account_data = json.load(f)
      if account_data['password'] == password:
         return account_data
      else:
         print("\033[31;1m用户或密码错误!\033[0m")
  else:
     print("\033[31;1m用户不存在!\033[0m")


def acc_login(user_data):
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count <3:
        user_name = raw_input("\033[32;1m用户名:\033[0m").strip()
        user_passwd = getpass.getpass("\033[32;1m密码:\033[0m")
        auth = acc_auth(user_name,user_passwd)
        if auth:
            ret_post_obj = operation.return_post()
            auth_post_data = ret_post_obj.get_auth_post(user_name,user_passwd)
            op_obj = operation.Action()
            auth_id = op_obj.get_auth_id(auth_post_data)
            user_data['is_authenticated'] = True
            user_data['account_id'] = user_name
            user_data['auth_id'] = auth_id
            return auth
        retry_count += 1
    else:
        print("\033[31;1m失败次数过多!\033[0m")
        exit()
