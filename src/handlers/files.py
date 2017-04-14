#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/14

import time
import logging

from tornado.web import RequestHandler
from src.utils import random_str


class File(object):
    def __init__(self, file_name, content):
        self._file_name = file_name
        self._content = content

    def _get_store_name(self):
        """获取新文件名称"""

        return random_str.get_random_str(20) + str(time.time())


class FilesHandler(RequestHandler):
    """处理上传文件"""

    def get(self):
        files = self.request.files["upload_file"]
        for file in files:
            pass
