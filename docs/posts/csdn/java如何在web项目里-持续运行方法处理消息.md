---
title: "Java如何在web项目里，持续运行方法处理消息"
date: 2021-06-15
description: "在ctwing平台遇到了问题，由于没有经验。很是困恼， 然年后从网上找到了相应的方法。第一步，将要运行的方法的类 实现runnable接口。第二步，实现listener 如图。第三步配置你的web.xml 。完成..."
tags:
  - CSDN迁移
---

# Java如何在web项目里，持续运行方法处理消息

###### 在ctwing平台遇到了问题，由于没有经验。很是困恼， 然年后从网上找到了相应的方法。

##### 第一步，将要运行的方法的类 实现runnable接口。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d276c4ab0931766bc6ce13a8c6ae677a.png)

#### 第二步，实现listener 如图。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3345316a90df56487b5f7f80b5c25e3f.png)

##### 第三步配置你的web.xml 。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4218629445efdf062539aff0197bf128.png)

## 完成
