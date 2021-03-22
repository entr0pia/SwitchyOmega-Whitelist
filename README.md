# SwitchyOmega-Whitelist
适用于 SwitchyOmega 的中国网站白名单，主要内容来自 [felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)，纯列表，持续更新。

## 使用步骤
1. 在 Chrome/Edge 中安装 [SwitchyOmega](https://chrome.google.com/webstore/detail/proxy-switchyomega/padekgcemlokbadohgkifijomclgjgif) 插件；
2. 在插件的设置中，点击「新增情景模式」-「代理服务器」，名字自己设置；
3. 点击「新增情景模式」-「自动切换」，名字自己设置；
4. 规则列表设置为直连；
5. 默认情景模式设置为刚才设置的代理服务器；
6. 点击「添加规则列表」，在规则列表网址，输入 [https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl](https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl)；
7. 点击「立即更新情景模式」；
8. 点击左上角「界面」，将初始情景模式改为「自动切换」。


## 使用建议
1. [黑名单](https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt) 适用于经常访问国内网的同学，白名单适用于经常访问国外网的同学；
2. 建议``google.cn``强制走代理。
3. 建议将以下地址加入【步骤2】中的“不代理的地址列表”：  
``<local>``  
``10.0.0.0/8``  
``172.16.0.0/12``  
``192.168.0.0/16``  
``fc00::/7``
