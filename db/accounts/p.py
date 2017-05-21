import json

acc_dic = {
    'id': 'admin',
    'password': 'DZaBBix@7T',
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}


res=json.dump(acc_dic,open('/zabbbix_api/db/accounts/admin','w'))

# with open('/root/ip', 'r') as f:
#     for i in f:
#         HostName = "tjkd_%s" % (i.strip("\n"))
#         IP = i.strip("\n")
#         self.post_data["params"]["host"] = HostName
#         self.post_data['params']['interfaces'][0]['ip'] = IP
#         ret = requests.post(self.url, data=json.dumps(self.post_data), headers=self.post_header)
#         zabbix_ret = json.loads(ret.text)
#         if not zabbix_ret.has_key('result'):
#             return zabbix_ret['error']['data']
#         else:
#             return zabbix_ret.get('result')