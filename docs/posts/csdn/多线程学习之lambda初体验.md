---
title: "多线程学习之lambda初体验"
date: 2021-05-28
tags:
  - CSDN迁移
---

# 多线程学习之lambda初体验

_**很多人对lambda表达式表示费解，很正常。一下是一些实例：**_  
lambda表达式 简化函数式接口实现的过程。  
函数式接口就是 该接口只有一个方法。就叫函数式接口

**1\. 首先来看看匿名内部类的写法**
    
    
    public class lambda {
        public static void main(String[] args) {
            runnable myrunnable=new runnable() {
                @Override
                public void run() {
                    System.out.println("hello world");
                }
            };
            myrunnable.run();
            
        }
        //定义一个runnable接口，里面包含一个run方法
        interface runnable{
            void run();
        }
    }
    

这里直接new了一个接口，没有类的名字所以为匿名内部类。

我们用lambda表达式来简化 代码如下：
    
    
    runnable lambda=()->{
                System.out.println("hello lambda ");
            };
            lambda.run();
    

这无疑极大的简化了书写。

**运行结果：**  
![在这里插入图片描述](/images/csdn/27b44da04ffd.png)
