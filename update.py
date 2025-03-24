#!/usr/bin/env python3
'''
@作者: 风沐白
@文件: update.py
@描述: 从网络来源更新白名单规则
'''

import requests
import re
import os
import time

up_time = time.ctime()
headline = ['[SwitchyOmega Conditions]\n',
            '; Require: https://github.com/zero-peak/ZeroOmega\n',
            '; Update @ {}\n'.format(up_time),
            '\n',
            '; cn域名都不走代理\n',
            '*.cn\n',
            '*.wang\n',
            '\n',
            '; 局域网IP不走代理\n',
            '10.*.*.*\n',
            '172.16.*.*\n',
            '172.17.*.*\n',
            '172.18.*.*\n',
            '172.19.*.*\n',
            '172.20.*.*\n',
            '172.21.*.*\n',
            '172.22.*.*\n',
            '172.23.*.*\n',
            '172.24.*.*\n',
            '172.25.*.*\n',
            '172.26.*.*\n',
            '172.27.*.*\n',
            '172.28.*.*\n',
            '172.29.*.*\n',
            '172.30.*.*\n',
            '172.31.*.*\n',
            '169.254.*.*\n',
            '192.168.*.*\n',
            '\n',
            '; 教育网\n',
            '*.acm.org\n',
            '*.dblp.org\n',
            '*.ebscohost.com\n',
            '*.edu\n',
            '*.edu.*\n',
            '*.engineeringvillage.com\n',
            '*.ieee.org\n',
            '*.jstor.org\n',
            '*.lexis.com\n',
            '*.msftconnecttest.com\n',
            '*.nature.com\n',
            '*.oclc.org\n',
            '*.proquest.com\n',
            '*.researchgate.net\n',
            '*.sciencedirect.com\n',
            '*.sciencemag.org\n',
            '*.springer.com\n',
            '*.tandfonline.com\n',
            '*.uni-trier.de\n',
            '*.webofknowledge.com\n',
            '*.wiley.com\n',
            '\n',
            '; 常规列表\n']

def main():
    # 来源 https://github.com/felixonmars/dnsmasq-china-list
    # 本地运行可能需要代理
    conf_url = 'https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf'
    conf_file = 'accelerated-domains.china.conf'
    sorl_file = 'white-list.sorl'
    rules = set()

    r = requests.get(conf_url)
    with open(conf_file, 'wb') as f:
        f.write(r.content)

    with open(conf_file, 'r') as f:
        for line in f.readlines():
            if line[0] == '#':
                continue
            rule = re.sub(r'server=/(\S+)/\d+\.\d+\.\d+\.\d+', r'*.\1', line)
            if re.match(r'^\*\.\w+$', rule):
                continue
            rules.add(rule)

    rules = list(rules)
    rules.sort()
    out = [*headline, *rules]

    with open(sorl_file, 'w') as f:
        f.writelines(out)

    os.remove(conf_file)




def mini():
    conf_url = 'https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/ChinaDomain.list'
    conf_file = 'ChinaDomain.list'
    sorl_file = 'white-mini.sorl'
    rules = []

    r = requests.get(conf_url)
    with open(conf_file, 'wb') as f:
        f.write(r.content)

    with open(conf_file, 'r') as f:
        for line in f.readlines():
            if line[0] == '#':
                continue
            if 'DOMAIN-SUFFIX' in line:
                rule = re.sub(r'^DOMAIN-SUFFIX,(\S+)$', r'*.\1', line)
            elif 'DOMAIN-KEYWORD' in line:
                rule = re.sub(r'^DOMAIN-KEYWORD,(\S+)$', r'*.\1.*', line)
            elif 'DOMAIN' in line:
                rule = re.sub(r'^DOMAIN,(\S+)$', r'\1', line)
            else:
                continue
            if re.match(r'^\*\.\w+$', rule):
                continue
            rules.append(rule)

    out = [*headline, *rules]

    with open(sorl_file, 'w') as f:
        f.writelines(out)

    os.remove(conf_file)


if __name__ == "__main__":
    main()
    mini()
