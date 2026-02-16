---
title: "targetinvocationexception 自己的小错误"
date: 2020-10-19
tags:
  - CSDN迁移
---

# targetinvocationexception 自己的小错误

用反射的时候 报了targetinvokeception查了百度 搞半天 结果发现自己没开 redis 服务器

开了以后报错  
java.lang.reflect.InvocationTargetException  
at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)  
at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)  
at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)。。。。  
然后在droid配置文件中加上 url末尾加上 allowPublicKeyRetrieval=true  
错误解决！！！ [转载自这篇文章](<https://blog.csdn.net/u013360850/article/details/80373604>)
