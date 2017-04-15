#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/14
from tornado.web import URLSpec
from handlers import files

urls = [URLSpec("/file", files.FilesHandler)]
