#!/usr/bin/env python3
'''
@作者: 风沐白
@文件: update.py
@描述: 从网络来源更新白名单规则
'''

import requests
import re
import os

# 默认来源 git@github.com:felixonmars/dnsmasq-china-list.git, 可能需要代理
confurl = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf'

if __name__ == "__main__":
    conffile = 'accelerated-domains.china.conf'
    sorlfile = 'white-list.sorl'
    rules = set()
    headline = ['[SwitchyOmega Conditions]\n',
                '; Require: SwitchyOmega >= 2.3.2\n',
                '\n',
                '; cn域名都不走代理\n',
                '*.cn\n',
                '\n',
                '; 数字开头不走代理\n',
                '1*.*.*.*\n',
                '2*.*.*.*\n',
                '3*.*.*.*\n',
                '4*.*.*.*\n',
                '5*.*.*.*\n',
                '6*.*.*.*\n',
                '7*.*.*.*\n',
                '8*.*.*.*\n',
                '9*.*.*.*\n',
                '\n',
                '; 教育网\n',
                '*.acm.org\n',
                'dblp.org\n',
                '*.edu\n',
                '*.edu.*\n',
                '*.ieee.org\n',
                '*.msftconnecttest.com\n',
                '*.springer.com\n',
                '*.uni-trier.de\n',
                '*.webofknowledge.com\n',
                '\n']

    r = requests.get(confurl)
    with open(conffile, 'wb') as f:
        f.write(r.content)

    with open(conffile, 'r') as f:
        for line in f.readlines():
            if line[0] == '#':
                continue
            rules.add(re.sub(r'server=/(\S+)/\d+\.\d+\.\d+\.\d+', r'*.\1', line))

    rules = list(rules)
    rules.sort()
    out = [*headline, *rules]

    with open(sorlfile, 'w') as f:
        f.writelines(out)

    os.remove(conffile)
