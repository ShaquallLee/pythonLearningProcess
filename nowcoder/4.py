#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: 4.py
# @time: 2020/2/5 0005 11:57
# @desc:


while True:
    try:
        N = int(input())
        if N > 1000:
            N = 1000
        arr = [i for i in range(N)]
        i = 0
        count = 0
        while len(arr) > 1:
            i +=1
            if i >= len(arr):
                i -= len(arr)
            count += 1
            if count == 2:
                arr.pop(i)
                count = 0
        print(arr[0])
    except:
        break
