---
title: "shiro学习之错误 No realms have been configured! One or more realms must be present to execute an authori"
date: 2021-06-04
description: "看老师的配置文件，配置授权的时候忘记写如下配置：出现错误：No realms have been configured!  One or more realms must be present to execute an authorization operation.要使用授权功能 必须在securityManager中 加入realms （多realm情况下）同时有以下配置：..."
tags:
  - CSDN迁移
---

# shiro学习之错误 No realms have been configured! One or more realms must be present to execute an authori

看老师的配置文件，配置授权的时候忘记写如下配置：

出现错误：  
No realms have been configured! One or more realms must be present to execute an authorization operation.  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/7f7da2389b7180e9546099ff1f71d54a.png)  
要使用授权功能 必须在securityManager中 加入realms （多realm情况下）  
同时有以下配置：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5335d2a03ab0b1576b28d6a305ef27c7.png)
