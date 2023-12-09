#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： sunhb
# datetime： 2023/11/2 下午4:48 
# ide： PyCharm
# filename: operate_json_test.py
def test_operate_json():
    from yantu_python_util.operate_json import write_json
    write_json(["tes"],filepath="../test/test.json")
    pass

