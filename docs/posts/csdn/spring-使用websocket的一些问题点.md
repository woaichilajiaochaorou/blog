---
title: "Spring 使用websocket的一些问题点"
date: 2021-05-20
tags:
  - CSDN迁移
---

# Spring 使用websocket的一些问题点

首先我被Spring版本坑惨了，在使用5.3.6版本时，在配置websocketconfiger对象时加上configeration注解时启动项目 报错 no class  
然后我把版本更换成了5.3.3 重启问题解决 。

还有 html 访问 websocket的时候要注意路径问题，而且页面不能直接通过idea快捷方式打开 要在启动项目后、通过访问项目页面链接websocket 要不然报 websocket connection to **** failed
