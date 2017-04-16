#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/14

import base64

import settings

from tornado.web import RequestHandler

from services import file as file_service


class FilesHandler(RequestHandler):
    """处理上传文件"""

    def post(self):

        file_b64 = self.get_argument("file_b64")
        file_name = self.get_argument("file_name")
        file = base64.b64decode(file_b64)

        file_sv = file_service.FileService(file_name, file)
        file_sv.save(root_path=settings.static_root)

        return
