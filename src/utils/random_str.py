#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/14

import string
import random


def get_random_str(str_len):
    """获取随机字符串

    :param int str_len: 字符串长度
    :return:
        str 随机字符串
    """

    strings = string.ascii_letters + string.digits
    result = []
    while str_len > 0:
        index = random.randint(0, len(strings) - 1)
        result.append(strings[index])
        str_len -= 1
    return "".join(result)
