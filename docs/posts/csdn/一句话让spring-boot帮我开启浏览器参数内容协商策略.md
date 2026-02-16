---
title: "一句话让spring-boot帮我开启浏览器参数内容协商策略"
date: 2021-08-24
tags:
  - CSDN迁移
---

# 一句话让spring-boot帮我开启浏览器参数内容协商策略

## 一句话：

![在这里插入图片描述](/images/csdn/21cd49c3696f.png)

## 背后的原理：

##### 当我们开启参数协商以后在RequestResponseBodyMethodProcessor里 有个方法

![在这里插入图片描述](/images/csdn/99e17852fa03.png)  
有个writeWithMessageConverter 这里包含消息的读和写操作 进入查看发现：  
![在这里插入图片描述](/images/csdn/804c19603fb0.png)  
里面有个获取request的可以接受的类型 继续进入  
![在这里插入图片描述](/images/csdn/a2076da0c665.png)

调用了一个内容协商管理器的方法。进入方法  
![在这里插入图片描述](/images/csdn/cf2c95934243.png)  
此方法遍历所有的strategy 我们查看此时的策略发现  
![在这里插入图片描述](/images/csdn/0fdab753febb.png)  
此时存在两个策略一个是参数内容协商 另外是请求头内容协商。  
oh 原来当我们写下那句 **spring.mvc.contentnegotiation.favor-parameter=true**  
竟然会增加一种策略

咳咳，继续。。  
进入strategy.resolveMediaTypes查看发现：  
![在这里插入图片描述](/images/csdn/1c4900e5bc8a.png)  
调用了一个方法解析媒体类型key 其中有个参数getMediaTypeKey 点击进入  
![在这里插入图片描述](/images/csdn/2ad711a83e85.png)  
![在这里插入图片描述](/images/csdn/e0061b6c9f90.png)  
原来在这个策略里会找到我们发送的参数名字 format ohhhhh！

ok 回到这个参数策略的方法  
![在这里插入图片描述](/images/csdn/4a7ddc95e26e.png)  
进入这个方法  
![在这里插入图片描述](/images/csdn/786f8f7b2b39.png)

获得key对应的媒体类型 如果key的mediaType为空返回*/*
