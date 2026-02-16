---
title: "Spring的自动装配xml"
date: 2021-01-21
description: "Spring的自动装配autowire=“byName”意思是当bean中的引用类型的别名（例如 Dao dao=null dao就是别名）与 另外的bean的id 或者 name 相同则此bean被装配autowire=“byType”意思是当包含引用类型的bean 中的引用类型的class与另外一个bean标签属性的class属于同源关系就可以被包含引用类型的bean引用。同源关系的意思是：两"
tags:
  - CSDN迁移
---

# Spring的自动装配xml

### Spring的自动装配

autowire=“byName”  
意思是当bean中的引用类型的别名（例如 Dao dao=null dao就是别名）与 另外的bean的id 或者 name 相同则此bean被装配  
autowire=“byType”  
意思是当包含引用类型的bean 中的**引用类型的class** 与另外一个bean标签属性的class属于同源关系  
就可以被包含引用类型的bean引用。  
**同源关系的意思是** ：  
两个class 是父子关系，  
两个class相同，  
两个class是接口和实现类的关系
