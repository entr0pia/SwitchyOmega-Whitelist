# SwitchyOmega-Whitelist
适用于 SwitchyOmega 的中国网站白名单，主要内容来自 [felixonmars/dnsmasq-china-list](https://github.com/felixonmars/dnsmasq-china-list)，纯列表，自动更新。

**建议使用 [ZeroOmega](https://github.com/zero-peak/ZeroOmega) 插件，原版插件已遭到攻击。参考阅读 [When Chrome Extensions Turn Against Us: The Cyberhaven Breach and Beyond](https://medium.com/extensiontotal/when-chrome-extensions-turn-against-us-the-cyberhaven-breach-and-beyond-9e35e59e1bff)**

## 使用步骤
1. 安装 [ZeroOmega](https://github.com/zero-peak/ZeroOmega) 插件；
2. 在插件的设置中，点击「新增情景模式」-「代理服务器」，名字自己设置；
3. 点击「新增情景模式」-「自动切换」，名字自己设置；
4. 规则列表设置为直连；
5. 默认情景模式设置为刚才设置的代理服务器；
6. 点击「添加规则列表」，在规则列表网址，输入
    ```
    https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl
    ```
    > 代理加速 (一个一个试):
    > 1. https://ghproxy.com/https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl
    > 2. https://mirror.ghproxy.com/https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl
    > 3. https://ghproxy.net/https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl
    > 4. https://fastly.jsdelivr.net/gh/entr0pia/SwitchyOmega-Whitelist@master/white-list.sorl
    > 5. https://gcore.jsdelivr.net/gh/entr0pia/SwitchyOmega-Whitelist@master/white-list.sorl
    > 6. https://jsdelivr.b-cdn.net/gh/entr0pia/SwitchyOmega-Whitelist@master/white-list.sorl
    > 7. https://raw.fgit.cf/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl
    > 8. https://gh-proxy.com/https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-list.sorl

8. 点击「立即更新情景模式」；
9. 点击左上角「界面」，将初始情景模式改为「自动切换」。


## 使用建议
- [黑名单](https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt) 适用于经常访问国内网的同学，白名单适用于经常访问国外网的同学；
- 建议 `google.cn` 强制走代理。
- 建议将以下地址加入【步骤2】中的“不代理的地址列表”：
    ```
    <local>  
    fc00::/7  
    fe80::/10
    ```
- 遇到性能问题使用[mini](https://raw.githubusercontent.com/entr0pia/SwitchyOmega-Whitelist/master/white-mini.sorl)规则
