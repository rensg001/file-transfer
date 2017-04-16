#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/14

import os

curdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = "/".join(curdir.split("/")[:-1])

debug = True

static_root = os.path.join(parent_dir, "upload")
