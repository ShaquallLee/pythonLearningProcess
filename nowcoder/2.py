#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: 2.py
# @time: 2020/2/5 0005 11:04
# @desc:

while True:
    try:
        n = int(input())
        arr = []
        for i in range(n):
            a = int(input())
            if a not in arr:
                arr.append(a)
        arr.sort()
        print(n)
        for i in range(len(arr)):
            print(arr[i])
    except:
        break

# while True:
#     try:
#         n = int(input())
#         arr = []
#         for i in range(n):
#             a = int(input())
#             if a not in arr:
#                 arr.append(a)
#         arr.sort()
#         print(n)
#         for i in range(len(arr)):
#             print(arr[i])
#     except:
#         break
