---
title: "shiro学习之错误 No realms have been configured! One or more realms must be present to execute an authori"
date: 2021-06-04
tags:
  - CSDN迁移
---

# shiro学习之错误 No realms have been configured! One or more realms must be present to execute an authori

看老师的配置文件，配置授权的时候忘记写如下配置：

出现错误：  
No realms have been configured! One or more realms must be present to execute an authorization operation.  
![在这里插入图片描述](/images/csdn/9b0ac298f95a.png)  
要使用授权功能 必须在securityManager中 加入realms （多realm情况下）  
同时有以下配置：  
![在这里插入图片描述](/images/csdn/e32160905b72.png)
