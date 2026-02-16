---
title: "matlab代码打成jar包 并在idea中使用"
date: 2021-10-03
tags:
  - CSDN迁移
---

# matlab代码打成jar包 并在idea中使用

首先要保证电脑安装了jdk1.6（版本不能太高 我以2016的matlab为例）和matlab  
在matlab 命令行输入以下：  
![在这里插入图片描述](/images/csdn/0c0eb7399407.png)  
然后在cmd 窗口中输入  
![在这里插入图片描述](/images/csdn/7da05007ea1e.png)  
这里两个的版本要是一致的。

在matlab中输入  
![在这里插入图片描述](/images/csdn/ccdaf171e736.png)  
选择Library compiler  
![在这里插入图片描述](/images/csdn/fa1e12815623.png)  
![在这里插入图片描述](/images/csdn/b78cf2e82148.png)  
这里可以搜索其他的博主文章来操作（我的不详细）；  
点击绿色对勾 打包  
**切记切记**  
**记得用管理员运行matlab要不然会报错**

然后把生成的jar包放到idea，而且还需要安装MCR  
然后 还要在项目中再加一个jar包  
![在这里插入图片描述](/images/csdn/ed8a9cf35c6b.png)  
路径在matlab的MCR的toolbox的javabuilder中  
两个jar包如图所示 一个是Javabuilder一个是你自己的jar。  
![在这里插入图片描述](/images/csdn/2b3ecf32f86e.png)  
然后 调用  
![在这里插入图片描述](/images/csdn/b4a0bba1d4e9.png)

方法返回值可以按照我这样来处理。
