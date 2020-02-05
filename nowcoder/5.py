#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: 5.py
# @time: 2020/2/5 0005 12:08
# @desc:



import sys
while True:
    try:
        s = input()
        arr = []
        for x in list(s):
            if x not in arr:
                sys.stdout.write(x)
                arr.append(x)
        sys.stdout.write('\n')
    except:
        break
