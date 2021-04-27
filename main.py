#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from litxsscjd.user import litUesr
import time

def logcat(msg, level='I'):
    print('%s %s: %s' % (time.ctime().split(' ')[-2], level, msg))

litu = litUesr("B19071121","xxxxxx")

if litu.is_logged:
    logcat("登陆成功!")
    logcat("用户名: %s" % litu.info['userName'] )
    logcat("正在查找答题记录...")
else:
    logcat("登陆失败: %s " % litu.login['message'],'E')



