#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/14

from tornado import httpserver
from tornado import ioloop
from tornado.web import Application

from src.routes import urls


def main():
    app = Application(handlers=urls)
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()
