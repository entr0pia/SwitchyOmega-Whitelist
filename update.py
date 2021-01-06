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
    r = requests.get(confurl)
    conffile = 'accelerated-domains.china.conf'
    sorlfile = 'white-list.sorl'
    with open(conffile, 'wb') as f:
        f.write(r.content)

    headline = []
    rules = set()

    with open(sorlfile, 'r') as f:
        for line in f.readlines():
            if re.match(r'\*\.\S+\.\S+', line) == None:
                headline.append(line)
            else:
                break

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
