#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auhthor:crstly
import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)
print sys.path
from core import main

if __name__ == '__main__':
    program = main.API()
    program.run()
