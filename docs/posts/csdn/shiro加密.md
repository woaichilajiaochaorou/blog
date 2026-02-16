---
title: "shiro加密"
date: 2021-06-02
tags:
  - CSDN迁移
---

# shiro加密

1.如何把一个字符串加密为MD5  
2\. 替换当前realm的credentialManager 属性直接使用hashedCredentialMatcher并设置属性 加密算法即可。  
**配置如下：**  
![在这里插入图片描述](/images/csdn/ba78720ebe16.png)

**比较的步骤**  
首先在getpassword打个断点  
![在这里插入图片描述](/images/csdn/502973afd875.png)  
下一步进入这个方法 设置credential为password  
![在这里插入图片描述](/images/csdn/6f8676c5a0c7.png)

接下来对token的credential进行加密。也就是对password  
![在这里插入图片描述](/images/csdn/760ac4df3d06.png)  
下一步对token 加密后的值与info的credentials进行比较。可以看出调用了equals方法。  
![在这里插入图片描述](/images/csdn/314ef4fedc1a.png)
