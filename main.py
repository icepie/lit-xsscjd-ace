#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pickle
from litxsscjd.user import litUesr
import time

CONFIG = {
    'username': 'B19000000', # 帐号
    'password': '123456', # 密码
    'dotime': 256, #完成用时 (秒), 建议三十分钟以内
    'score': 99 #想达到多少分以上?
}

def logcat(msg, level='I'):
    print('%s %s: %s' % (time.ctime().split(' ')[-2], level, msg))

def save_obj(obj, name: str):
    with open('obj/'+ name + '.py', 'w', encoding='utf-8') as f:
        f.write(str(obj))

def load_obj(name: str):
    with open('obj/' + name + '.py', encoding='utf-8') as f:
        d = eval(f.read())  # eval
    return d

litu = litUesr(CONFIG['username'],CONFIG['password'])

if litu.is_logged:
    logcat("登陆成功!")
    logcat("用户名: %s" % litu.info['userName'] )
    logcat("正在查找答题记录...")
    records = litu.get_record()
    if records['code'] == 1:
        logcat("查找到 %s 次答题记录" % len(records['response']))
        r_count = 0
        for r in records['response']:
            print("记录: %s \t 分数: %s \t 完成时间: %ss \t 日期: %s" % (r_count, r['userScore'], r['doTime'],r['date']))
            r_count=r_count+1

        input("按回车键开始添加一次答题记录...")

        # 要跑旧试卷的话...从这里开始注释掉
        #####
        logcat("准备获取新试卷...")
        paper = litu.get_exam_paper()
        #print(paper)
        if paper['code'] == 1:
            p_id=paper['response']['id']
            logcat("获取成功")
            logcat("试卷id: %s" % p_id)
            logcat("正在缓存试卷...(以防万一)")
            save_obj(paper,str(paper['response']['id']))
        else:
            logcat("获取失败!", "E")
        #####
        # 这里结束

        # 跑旧试卷这里开始去掉注释, id换成obj目录下的历史试卷
        #####
        # p_id=9826
        # logcat("准备获取旧试卷(id: %s)" % str(p_id))
        # paper = load_obj(str(p_id))
        #####
        # 这里结束

        # 构造单题目回答
        # 单选: {"questionId":2105,"content":"A","contentArray":[],"completed":true,"itemOrder":1
        # 多选: {"questionId":2190,"content":null,"contentArray":["B","A","C","D"],"completed":true,"itemOrder":21},
        # 判断: {"questionId":2509,"content":"A","contentArray":[],"completed":true,"itemOrder":31},
        # 填空: {"questionId":2838,"content":null,"contentArray":["xxxx"],"completed":true,"itemOrder":46},
        # answer_data = {
        #     'questionId': '',
        #     'content': None,
        #     'contentArray': [],
        #     'completed': True,
        #     'itemOrder': 0
        # }
        # 构造回答
        answer_data = {
            'questionId': None,
            'doTime': CONFIG['dotime'],
            'answerItems': [],
            "id": p_id
        }

        for p in paper['response']['titleItems']:
            if p['name'] == '单选题':
                logcat("正在分析单选题...")
                for q  in (p['questionItems']):
                    #print(q)
                    answer = {
                        'questionId': q['id'],
                        'content': 'E',
                        'contentArray': [],
                        'completed': True,
                        'itemOrder': q['itemOrder']
                    }
                    answer_data['answerItems'].append(answer)
                    pass

            if p['name'] == '多选题':
                logcat("正在分析多选题...")
                for q  in (p['questionItems']):
                    answer = {
                        'questionId': q['id'],
                        'content': None,
                        'contentArray': ['A','E'],
                        'completed': True,
                        'itemOrder': q['itemOrder']
                    }
                    answer_data['answerItems'].append(answer)
                    pass

            if p['name'] == '判断题':
                logcat("正在分析判断题...")
                for q  in (p['questionItems']):
                    answer = {
                        'questionId': q['id'],
                        'content': '',
                        'contentArray': [],
                        'completed': True,
                        'itemOrder': q['itemOrder']
                    }
                    answer_data['answerItems'].append(answer)
                    pass

            if p['name'] == '填空题':
                logcat("正在分析填空题...")
                for q  in (p['questionItems']):
                    answer = {
                        'questionId': q['id'],
                        'content': None,
                        'contentArray': [],
                        'completed': True,
                        'itemOrder': q['itemOrder']
                    }
                    for c in q['items']:
                        answer['contentArray'].append(c['content'])
                    answer_data['answerItems'].append(answer)
                    pass

        logcat("构造回答数据成功!")

        sc = 0
        qc = 0
        qp = 0 # 题目验证进度
        qp_tmp = 1
        logcat("准备开始第 %d 次提交..." % sc)
        
        rte = litu.submit_exam_answer(answer_data)

        if rte['code'] == 1:
            #print(rte)
            logcat("提交成功!")
            qc = rte['response']['questionCorrect']
            us = rte['response']['userScore']
            logcat("分数: %s \t 正确数: %s" % (us, qc))
        else:
            logcat("提交失败!", "E")
            logcat("自动退出")
            exit()

        # 刷分模式
        fc=0
        while not (us >= CONFIG['score']):
            sc=sc+1
            logcat("正在调整参数...", )
            
            if qp < 20:
                answer_data_tmp = answer_data
                c = answer_data_tmp['answerItems'][qp]['content']
                print(c)
                if c == 'A':
                    answer_data_tmp['answerItems'][qp]['content']='B'
                elif c == 'B':
                    answer_data_tmp['answerItems'][qp]['content']='C'
                elif c == 'C':
                    answer_data_tmp['answerItems'][qp]['content']='D'
                else:
                    answer_data_tmp['answerItems'][qp]['content']='A'

            elif qp >= 20 and qp < 25:
                answer_data_tmp = answer_data
                # [[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')], [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')], [('A', 'B', 'C', 'D')]]
                c = answer_data_tmp['answerItems'][qp]['contentArray']
                print(c)
                if c == ['A','B']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A','C']
                elif c == ['A','C']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A','D']
                elif c == ['A','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['B','C']
                elif c == ['B','C']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['B','D']
                elif c == ['B','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['C','D']
                elif c == ['C','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A','B','C']
                elif c == ['A','B','C']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A','B','D']
                elif c == ['A','B','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A', 'C', 'D']
                elif c == ['A','C','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['B', 'C', 'D']
                elif c == ['B','C','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A','B', 'C', 'D']
                elif c == ['A','B','C','D']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A']
                elif c == ['A']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['B']
                elif c == ['B']:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['C']
                else:
                    answer_data_tmp['answerItems'][qp]['contentArray']=['A','B']

            elif qp >= 25 and qp < 40:
                answer_data_tmp = answer_data
                c = answer_data_tmp['answerItems'][qp]['content']
                print(c)
                if c == 'A':
                    answer_data_tmp['answerItems'][qp]['content']='B'
                else:
                    answer_data_tmp['answerItems'][qp]['content']='A'
            elif qp >= 40:
                qb = 50
            
            logcat("准备开始第 %d 次提交..." % sc)
            rte = litu.submit_exam_answer(answer_data_tmp)

            if rte['code'] == 1:
                #print(rte)
                logcat("提交成功!")
                usn = rte['response']['userScore']
                qcn = rte['response']['questionCorrect']
                logcat("分数: %s \t 题目进度: %s \t 正确数: %s" % (usn, qp+11, qcn))
            else:
                logcat("提交失败!", "E")
                logcat("自动退出")
                exit()

            # 有些臭题处理一下
            if qcn > qc:
                fc = 0
                qc = qcn
                us = usn
                qp=qp+1
                answer_data = answer_data_tmp
            if qc >= 166:
                qb = 50

            #print(us,usn,qp)
        logcat("准备开始最后一次提交...")
        
        rte = litu.submit_exam_answer(answer_data)

        if rte['code'] == 1:
            #print(rte)
            logcat("提交成功!")
            qc = rte['response']['questionCorrect']
            us = rte['response']['userScore']
            logcat("分数: %s \t 正确数: %s" % (us, qc))
        else:
            logcat("提交失败!", "E")
            logcat("自动退出")
            exit()
        logcat("本次答题结束!")
        #print(answer_data)
    else:
        logcat("查找失败!", "E")

else:
    logcat("登陆失败!",'E')



