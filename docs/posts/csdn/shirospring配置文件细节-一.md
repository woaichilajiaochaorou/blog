---
title: "shirospring配置文件细节（一）"
date: 2021-05-31
tags:
  - CSDN迁移
---

# shirospring配置文件细节（一）

1. 在配置文件中，< bean id=“shiroFilter”> 必须和web  
.xml的shiroFilter的名字保持一致
  2. 其中shiro-spring配置文件里的shiroFilter的property标签内，遵循第一个首先配置原则，例如：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a1e5a858c51755c6dd397c141813765f.png)  
如果首先写了 /**=anon 则后面再写 /index.html=authc 被无效化。所有页面可以访问。
