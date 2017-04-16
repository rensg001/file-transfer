#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from models import bases
from sqlalchemy import Column, String, Boolean


class FileModel(bases.TimeStampWithIDMixin, bases.BaseModel):
    __tablename__ = "files"

    name = Column(String(256), nullable=False)
    path = Column(String(512), nullable=False)
    isvalid = Column(Boolean, default=True, nullable=False)
