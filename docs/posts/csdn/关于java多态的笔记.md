---
title: "关于Java多态的笔记"
date: 2020-06-05
description: "面向对象的三大特征：继承 extends，封装，多态。多态：父类引用子类对象老毕说的：编译看左边 运行看右边什么意思呢？public class demo {    public static void main(String[] args) {        fu son =new zi();        son.method();//如果父类方法被子类重写则优先调用子类方法    }}pub"
tags:
  - CSDN迁移
---

# 关于Java多态的笔记

**面向对象的三大特征：**  
继承 extends，封装，多态。  
多态：父类引用子类对象

**老毕说的：编译看左边 运行看右边**  
什么意思呢？
    
    
    public class demo {
        public static void main(String[] args) {
            fu son =new zi();
            son.method();//如果父类方法被子类重写则优先调用子类方法
        }
    }
    public  class fu {
    
        public void method(){
            System.out.println("父类方法");
        }
        public void methodfu(){
            System.out.println("父类方法");
        }
    
    }
    public class zi extends fu{
        private int age=66;
        private int num=20;
        public void method(){
            System.out.println("子类方法");
        }
    
    }
    
    

**fu son= new zi();**  
1.对于成员变量全看等号左边  
2.对于成员方法 如果没有编译看左边（要符合父类方法定义） 运行看右边（如果被子类重写覆盖则看右边）
