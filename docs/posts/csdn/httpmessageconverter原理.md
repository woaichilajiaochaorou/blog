---
title: "HttpMessageConverter原理"
date: 2021-08-23
tags:
  - CSDN迁移
---

# HttpMessageConverter原理

## 1.判断当前响应是否有了确定的媒体类型。

![在这里插入图片描述](/images/csdn/68fe23ede185.png)

## 2.获取客户端支持的接受类型。（header accept 字段 ）

![在这里插入图片描述](/images/csdn/26bcd1bbb0a0.png)  
这里用postman故意设置为xml  
然后找到一个合适的converter进行write  
![在这里插入图片描述](/images/csdn/11b9e072edf2.png)
