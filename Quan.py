# -*- coding:utf-8 -*-
# __author__ = 'kohna'

import qqlib
from time import sleep


def getbkn(self):  # Get the bkn
    skey = ''
    ha = 5381
    for itm in self:
        if itm.name == 'skey':
            skey = itm.value

    for tem in skey:
        ha += (ha << 5) + ord(tem)

    return ha & 0x7fffffff


if __name__ == '__main__':
    signurl = 'http://qiandao.qun.qq.com/cgi-bin/sign'  # the sign link
    q = 1234567  # raw_input(u"输入你的QQ: ")
    m = '1230000'  # raw_input(u"输入你的密码: ")
    qq = qqlib.QQ(q, m)
    qq.login()
    headr = {
        'Content-Type': 'text/plain;charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.59 QQ/7.5.15445.201 Safari/537.36'
    }
    qq.session.headers = headr
    qunnum = {'1234567', '2222222'}
    bkn = getbkn(qq.session.cookies)
    for isa in qunnum:
        sleep(1)
        ds = {'gc': isa,
              'is_sig': 0,
              'bkn': bkn,
              }     # Set POST data
        sc = qq.session.post(url=signurl, data=ds)  # Start Post data
        print sc.text.encode('unicode-escape')
