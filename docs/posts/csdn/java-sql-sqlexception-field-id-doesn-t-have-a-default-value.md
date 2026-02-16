---
title: "java.sql.SQLException: Field ‘id‘ doesn‘t have a default value"
date: 2022-12-30
tags:
  - CSDN迁移
---

# java.sql.SQLException: Field ‘id‘ doesn‘t have a default value

## java.sql.SQLException: Field ‘id’ doesn’t have a default value

* * *

在开发瑞吉外卖时遇到的错误，原因是数据库员工表id字段未设置自增，在yml中的mybatis-plus插件中设置数据库自增，调用mp的save时，问题得以解决。  
![在这里插入图片描述](/images/csdn/3c1056399515.png)
    
    
    mybatis-plus:
      configuration:
        map-underscore-to-camel-case: true
        log-impl: org.apache.ibatis.logging.stdout.StdOutImpl
      global-config:
        db-config:
          id-type: auto
          ```
