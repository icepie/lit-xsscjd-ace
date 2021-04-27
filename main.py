#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from litxsscjd.user import litUesr
import time

def logcat(msg, level='I'):
    print('%s %s: %s' % (time.ctime().split(' ')[-2], level, msg))

litu = litUesr("B19070404","xxxx")
#litu = litUesr("B19071121","xxxx")

if litu.is_logged:
    logcat("登陆成功!")
    logcat("用户名: %s" % litu.info['userName'] )
    logcat("正在查找答题记录...")
    records = litu.get_record()
    if records['code'] == 1:
        logcat("查找到 %s 次答题记录" % len(records['response']))
        r_count = 0
        for r in records['response']:
            print("记录: %s \t 分数: %s \t 完成时间: %s \t 日期: %s" % (r_count, r['userScore'], r['doTime'],r['date']))
            r_count=r_count+1

    else:
        logcat("查找失败!", "E")

else:
    logcat("登陆失败: %s " % litu.login['message'],'E')



