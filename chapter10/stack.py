#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhuzhengwei'

class Stack(object):
    def __init__(self):
        self.s = []


    def push(self,x):
        self.s.append(x)
        return

    def pop(self):
        return self.s.pop()