#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from core import db_handler
from config import settings

def load_current_balance(account_id):
  db_path = db_handler.db_handler(settings.DATABASE)
  account_file = "%s/%s" %(db_path,account_id)
  with open(account_file) as f:
    acc_data = json.load(f)
    return acc_data

