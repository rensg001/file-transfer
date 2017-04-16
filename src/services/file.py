#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import os
import datetime
import time
import logging

from utils import random_str


logger = logging.getLogger(__name__)


class FileService(object):
    def __init__(self, file_name, content):
        self._file_name = file_name
        self._content = content
        self._ext = None
        self._new_file_name = self._get_new_name()

    def get_path(self):
        """生成文件存储路径，此路径是增加日期目录分割并替换文件名称之后的路径

        Returns:
            str: 存储路径
        """

        today = datetime.date.today()
        date_list = [str(today.year), str(today.month), str(today.day)]
        dirictory = "/".join(date_list)
        return os.path.join(dirictory, self._new_file_name)

    def _get_ext(self):
        fragments = self._file_name.split(".")
        return fragments[-1]

    def _get_new_name(self):
        """获取新文件名称"""

        return random_str.get_random_str(20) + str(int(time.time())) + "." + self.ext

    def _create_dir(self, path):
        """如果目录不存在则创建目录

        Args:
            path: 文件路径

        Returns:

        """

        file_dir_list = path.split("/")[:-1]
        file_dir = "/".join(file_dir_list)
        try:
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
        except IOError:
            logger.error("Failed to create dir %s" % file_dir, exc_info=True)
            raise

    def save(self, root_path):
        """

        Args:
            root_path: 文件保存根路径

        Returns:

        Raises:
                文件保存失败抛出IOError异常

        """

        abs_path = os.path.join(root_path, self.get_path())
        self._create_dir(abs_path)

        try:
            with open(abs_path, mode="wb+") as file:
                file.write(self._content)
        except IOError:
            logger.error("save file error", exc_info=True)
            raise

    @property
    def ext(self):
        if self._ext is None:
            self._ext = self._get_ext()
        return self._ext