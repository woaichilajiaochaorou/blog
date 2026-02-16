---
title: "Java如何在web项目里，持续运行方法处理消息"
date: 2021-06-15
tags:
  - CSDN迁移
---

# Java如何在web项目里，持续运行方法处理消息

###### 在ctwing平台遇到了问题，由于没有经验。很是困恼， 然年后从网上找到了相应的方法。

##### 第一步，将要运行的方法的类 实现runnable接口。

![在这里插入图片描述](/images/csdn/d94a43988193.png)

#### 第二步，实现listener 如图。

![在这里插入图片描述](/images/csdn/006eb2aeac6f.png)

##### 第三步配置你的web.xml 。

![在这里插入图片描述](/images/csdn/f8286db273a2.png)

## 完成
