#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime


class TimeStampMixin(object):
    """时间戳mixin"""

    update_time = Column(DateTime, nullable=True)
    create_time = Column(DateTime, default=func.now())


class TimeStampWithIDMixin(TimeStampMixin):
    """使用id字段做主键的时间戳mixin"""

    id = Column(Integer, primary_key=True, autoincrement=True)


BaseModel = declarative_base()
