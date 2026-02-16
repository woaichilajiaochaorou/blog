---
title: "spring注解基础"
date: 2021-01-22
tags:
  - CSDN迁移
---

# spring注解基础

### spring注解注入基础

**@component** ：创建对象的 等同于< bean>的功能  
《bean id=“mystudent” class=“包路径.类名”》

属性：value 就是对象的名称 也就是bean的id值  
value值是唯一的，创建的对象在容器中只有一份  
放置的位置：在类的上面。

**@repository** 用于dao类表示此类能访问数据库  
**@service** 表示的类适用于业务处理可以有事务的功能

**@Controller** 用于控制器上 创建控制器对象能够接受用户的请求参数 显示请求的处理结果  
这几个注解的用法和component一样 都能创建对象但是有额外的功能。

**@AutoWired** 注解默认是**byType** 自动注入。  
有三种方式 ：  
1，在属性上  
2，在set方法上  
3，在构造方法上  
如果要指定byName 则需要两个注解  
**@AutoWired** 和**@Qualifier（“bean的id”）**与@**Component(“bean的id”)**相配合  
则可以指定该id的bean被自动装配

**@AutoWired** 有一个**required** 是一个**Boolean** 类型 此时表示该bean必须存在否则注入失败报错  
设置为false后 若不存在则不进行报错 设置该bean为null 。

**@resource的用法**

**@resource** 注解 jdk中的注解，默认使用byName自动装配，如果失败则在进行byType。
