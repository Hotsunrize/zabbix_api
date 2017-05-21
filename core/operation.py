#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from config import settings
import threading
import time

class return_post:

  def __init__(self):
    pass

  def get_auth_post(self,user,password):
    post_data = settings.auth_post_data
    post_data['params']['user'] = user
    post_data['params']['password'] = password
    return post_data

  def get_create_post(self,auth_id):
    post_data = settings.create_post_data
    post_data['auth'] = auth_id
    return post_data

  def get_info_post(self,auth_id):
    post_data = settings.get_gid_post_data
    post_data['auth'] = auth_id
    return post_data




class Action:
  err_info = {}
  suc_info = {}
  def __init__(self,post_header=settings.post_header,url=settings.url):
    self.__post_header = post_header
    self.__url = url

  def get_res(self,post_data):
    ret = requests.post(self.__url, data=json.dumps(post_data), headers=self.__post_header)
    txt_ret = json.loads(ret.text)
    return txt_ret 
  
  def create_run(self,i,post_data,err_info,suc_info):
    HostName = "tjkd_%s" % (i.strip("\n"))
    IP = i.strip("\n")
    post_data["params"]["host"] = HostName
    post_data['params']['interfaces'][0]['ip'] = IP
    zabbix_ret = self.get_res(post_data)
    if not zabbix_ret.has_key('result'):
      err_info[IP] = ["error",zabbix_ret['error']['data']]
    else:
      suc_info[IP] = ["success",zabbix_ret.get('result')]

    
  def create(self,post_data):
    t_objs  = []
    with open('/root/ip', 'r') as f:
      suc_info = {}
      err_info = {}
      for i in f:
        t = threading.Thread(target=self.create_run, args=(i,post_data,err_info,suc_info))
        t.start()
        t_objs.append(t)
      for t in t_objs:
        t.join()
    return err_info,suc_info


  def get_auth_id(self,post_data):
    zabbix_ret = self.get_res(post_data)
    return zabbix_ret.get('result')

  def get_info(self,post_data):
    zabbix_ret = self.get_res(post_data)
    if not zabbix_ret.has_key('result'):
      print 'get info error'
    else:
      RES=zabbix_ret.get('result')
      for i in RES:
        print i['name'],i['groupid'] 
