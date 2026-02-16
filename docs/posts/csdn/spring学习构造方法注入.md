---
title: "spring学习构造方法注入"
date: 2021-01-21
tags:
  - CSDN迁移
---

# spring学习构造方法注入

在spring中xml标签里用< constructor-arg>标签来表示一个构造方法的参数。

< constructor-arg>标签属性：  
name ：表示构造方法的形参  
index：表示构造方法的参数的位置 参数从左往右 0. 1 . 2  
value ：构造方法的参数是简单类型value  
ref：用于参数是引用类型，使用ref
