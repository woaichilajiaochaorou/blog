---
title: "一句话让spring-boot帮我开启浏览器参数内容协商策略"
date: 2021-08-24
tags:
  - CSDN迁移
---

# 一句话让spring-boot帮我开启浏览器参数内容协商策略

## 一句话：

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0e6aa4c8f3d703b58f78de64560a09df.png)

## 背后的原理：

##### 当我们开启参数协商以后在RequestResponseBodyMethodProcessor里 有个方法

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0fcb60f731a6f571fc5dfbcae18ddac6.png)  
有个writeWithMessageConverter 这里包含消息的读和写操作 进入查看发现：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1db7ab7757481891de883a1b5c8da72a.png)  
里面有个获取request的可以接受的类型 继续进入  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/200ab415bea73d5e2de69fd3852120be.png)

调用了一个内容协商管理器的方法。进入方法  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3733b3834bcaaa0d1e3a71192711f2de.png)  
此方法遍历所有的strategy 我们查看此时的策略发现  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/04dfa73d6b6001d69a80171b0f0f230c.png)  
此时存在两个策略一个是参数内容协商 另外是请求头内容协商。  
oh 原来当我们写下那句 **spring.mvc.contentnegotiation.favor-parameter=true**  
竟然会增加一种策略

咳咳，继续。。  
进入strategy.resolveMediaTypes查看发现：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/43fcf032dc96f5c666d81b7a022156ca.png)  
调用了一个方法解析媒体类型key 其中有个参数getMediaTypeKey 点击进入  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/38258b38039c70593f8cdaae8652f66a.png)  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c78adcab70988b0305450a9c4c597e6e.png)  
原来在这个策略里会找到我们发送的参数名字 format ohhhhh！

ok 回到这个参数策略的方法  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/966ee61e82622a2197892cd342a3ce0b.png)  
进入这个方法  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3dac06d5b2624653992a63ed54bd5b85.png)

获得key对应的媒体类型 如果key的mediaType为空返回*/*
