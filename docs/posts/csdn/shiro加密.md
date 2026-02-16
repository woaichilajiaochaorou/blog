---
title: "shiro加密"
date: 2021-06-02
description: "1.如何把一个字符串加密为MD52.	替换当前realm的credentialManager 属性直接使用hashedCredentialMatcher并设置属性 加密算法即可。配置如下：比较的步骤首先在getpassword打个断点下一步进入这个方法 设置credential为password接下来对token的credential进行加密。也就是对password下一步对token 加密后的值"
tags:
  - CSDN迁移
---

# shiro加密

1.如何把一个字符串加密为MD5  
2\. 替换当前realm的credentialManager 属性直接使用hashedCredentialMatcher并设置属性 加密算法即可。  
**配置如下：**  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/fcd848b33ae3431ccc612f01aa47fcd9.png)

**比较的步骤**  
首先在getpassword打个断点  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c654949037ed7377fe869a0f477b35d1.png)  
下一步进入这个方法 设置credential为password  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2c0d4ee7859dc1653432986dcc19c69f.png)

接下来对token的credential进行加密。也就是对password  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4a7ea7e93e5b8291d23b595ed8e5f3dd.png)  
下一步对token 加密后的值与info的credentials进行比较。可以看出调用了equals方法。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1ce8ca758854026f2f12d14ea9ef8e5c.png)
