#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

url='http://61.153.111.215:88/zabbix/api_jsonrpc.php'
post_header = {'Content-Type': 'application/json'}

create_post_data = {
     "jsonrpc": "2.0",
     "method": "host.create",
     "params": {
     "host": "",
     "interfaces":[
        {
          "type": 1,
          "main": 1,
          "useip": 1,
          "ip": "",
          "dns": "",
          "port": "10050"
        }
                   ],
     "groups":[
        {
          "groupid": "35"
        }
                   ],
     "templates": [10105,10094],
},
        "auth": None,
        "id": 1
}

auth_post_data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": None,
        "password": None
    },
    "id": 1
}

get_gid_post_data=	{
    "jsonrpc": "2.0",
    "method": "hostgroup.get",
    "params": {
        "output": "extend",
    },
    "auth": None,
    "id": 1
}

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name':'accounts',
    'path': "%s/db" % BASE_DIR
}
