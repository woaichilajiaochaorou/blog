---
title: "初学反射之---类的加载于classLoader的理解"
date: 2021-07-13
tags:
  - CSDN迁移
---

# 初学反射之---类的加载于classLoader的理解

![在这里插入图片描述](/images/csdn/cbdbb7ae3d70.png)  
意思就是：  
将class文件加载进内存，生成Class对象 将二进制代码合并到jvm中，由jvm分配static的内存。将常量名替换成地址。  
然后将所有的类变量赋值动作和静态代码块中的语句合并，执行clinit方法；  
![在这里插入图片描述](/images/csdn/5a5575ac4ec5.png)
