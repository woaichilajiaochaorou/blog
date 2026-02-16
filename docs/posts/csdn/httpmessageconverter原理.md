---
title: "HttpMessageConverter原理"
date: 2021-08-23
tags:
  - CSDN迁移
---

# HttpMessageConverter原理

## 1.判断当前响应是否有了确定的媒体类型。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9d511a525c46449d0bfaa1deeb715afe.png)

## 2.获取客户端支持的接受类型。（header accept 字段 ）

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/29b52df68244b01c4d92abba86ee87f1.png)  
这里用postman故意设置为xml  
然后找到一个合适的converter进行write  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/66a8c085866c56170429c38c3d6a025b.png)
