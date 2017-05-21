#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
hadle all the database interactions
'''

def file_db_handle(conn_params):
  '''
  parse the db file path
  '''
  db_path='%s/%s' %(conn_params['path'],conn_params['name'])
  return db_path


def db_handler(conn_parms):
  if conn_parms['engine'] == 'file_storage':
    return file_db_handle(conn_parms)
  elif conn_parms['engine'] == 'mysql':
    pass
