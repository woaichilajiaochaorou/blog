---
title: "报错 An error happened during template parsing (template: “ServletContext resource [/shiroTest.html]“)"
date: 2021-06-06
tags:
  - CSDN迁移
---

# 报错 An error happened during template parsing (template: “ServletContext resource [/shiroTest.html]“)

使用thymeleaf视图解析器 这是因为模板解析器出现了错误  
刚上手thymeleaf不会用  
**解决办法：**

在方法上面加上@ResponseBody  
![在这里插入图片描述](/images/csdn/56b95e98fdfc.png)
