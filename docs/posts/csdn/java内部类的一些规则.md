---
title: "Java内部类的一些规则"
date: 2020-06-27
description: "public class outer {    int num=30;//外部类成员变量    public void method(){        int num=20;        class inner{//局部内部类什么修饰符都不能写                    //外部类public /default                    //成员内部类修饰符都可以写  "
tags:
  - CSDN迁移
---

# Java内部类的一些规则

public class outer {
    
        int num=30;//外部类成员变量
        public void method(){
            int num=20;
            class inner{//局部内部类什么修饰符都不能写
                        //外部类public /default
                        //成员内部类修饰符都可以写
                int num=10;
            }
            System.out.println(num);20
            System.out.println(this.num);30
            System.out.println(new inner().num);10
        }
    
     
    
    }
