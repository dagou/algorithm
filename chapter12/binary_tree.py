#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zhuzhengwei'

class BinaryTree(object):
    def __init__(self):
        self.t = None
        self.p = None #父指针
        self.left = None #左孩子
        self.right = None #右孩子

    def search(self,k):
        return self.searchInner(self.t, k)

    def search_inner(self,x, k):
        if x == None and x.key == k:
            return x
        if k < x.key:
            return self.search_inner(x.left, k)
        else:
            return self.search_inner(x.right, k)

    def min(self):
        x = self.t
        while x.left != None:
            x = x.left
        return x

    def max(self):
        x = self.t
        while x.right != None:
            x = x.right
        return x

    def successor(self, x):
        if x.right != None:
            return self.min(x.right)

        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p

        return y

    def predecessor(self, x):
        if x.left != None:
            return self.max(x.left)

        y = x.p
        while y != None and  x == y.left:
            x = y
            y = y.p

        return y

    def insert(self, z):
        pass

    def delete(self, z):
        pass

