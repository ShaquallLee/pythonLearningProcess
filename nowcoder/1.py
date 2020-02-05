#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: 1.py
# @time: 2020/2/5 0005 10:28
# @desc:

# import sys
#
# if __name__ == '__main__':
    # n = int(sys.stdin.readline().strip('\n'))
    # while n != 0:
    #     count = 0
    #     while 1:
    #         a = int(n / 3)
    #         b = n % 3
    #         count += a
    #         n = a + b
    #         if n == 2:
    #             count += 1
    #             break
    #         elif n < 2:
    #             break
    #     sys.stdout.write(str(count)+'\n')
    #     n = int(sys.stdin.readline().strip('\n'))
while True:
    try:
        n = int(input())
        count = 0
        while 1:
            a = int(n / 3)
            b = n % 3
            count += a
            n = a + b
            if n == 2:
                count += 1
                break
            elif n < 2:
                break
        print(count)
    except:
        break
