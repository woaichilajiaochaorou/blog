---
title: "matlab代码打成jar包 并在idea中使用"
date: 2021-10-03
description: "首先要保证电脑安装了jdk1.6（版本不能太高 我以2016的matlab为例）和matlab在matlab 命令行输入以下：然后在cmd 窗口中输入这里两个的版本要是一致的。在matlab中输入选择Library compiler这里可以搜索其他的博主文章来操作（我的不详细）；点击绿色对勾 打包然后把生成的jar包放到idea，而且还需要安装MCR然后 还要在项目中再加一个jar包路径在matl"
tags:
  - CSDN迁移
---

# matlab代码打成jar包 并在idea中使用

首先要保证电脑安装了jdk1.6（版本不能太高 我以2016的matlab为例）和matlab  
在matlab 命令行输入以下：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3293a8794c77434afaa2a4b7ae85e2a6.png)  
然后在cmd 窗口中输入  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e847f454070de05e0ffdefbce03d3d9c.png)  
这里两个的版本要是一致的。

在matlab中输入  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/11ede451f73fbf08c0e2d68c4da9514c.png)  
选择Library compiler  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2e42ba802c8a20eb4439d35faa60c23b.png)  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9cf80f837b0f7944b84186a2c4e0f590.png)  
这里可以搜索其他的博主文章来操作（我的不详细）；  
点击绿色对勾 打包  
**切记切记**  
**记得用管理员运行matlab要不然会报错**

然后把生成的jar包放到idea，而且还需要安装MCR  
然后 还要在项目中再加一个jar包  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c084b9e0bf5a3a587d8f955a079a01c2.png)  
路径在matlab的MCR的toolbox的javabuilder中  
两个jar包如图所示 一个是Javabuilder一个是你自己的jar。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/19e3454f4dec295754eb139fd1e9db38.png)  
然后 调用  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/591d5558af5fc17317b80b31d32acb97.png)

方法返回值可以按照我这样来处理。
