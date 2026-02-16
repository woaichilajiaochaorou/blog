---
title: "html 使用shiro标签 thymeleaf"
date: 2021-06-13
description: "这是spring.xml的配置文件，<!--使用thyme leaf-->    <!--视图解析器-->    <bean id='templateResolver' class='org.thymeleaf.spring5.templateresolver.SpringResourceTemplateResolver'>        <property name='prefix' value"
tags:
  - CSDN迁移
---

# html 使用shiro标签 thymeleaf

## 这是spring.xml的配置文件，
    
    
    <!--使用thyme leaf-->
        <!--视图解析器-->
        <bean id="templateResolver" class="org.thymeleaf.spring5.templateresolver.SpringResourceTemplateResolver">
            <property name="prefix" value="/"></property>
            <property name="suffix" value=".html"></property>
            <property name="templateMode" value="HTML"></property>
            <property name="cacheable" value="false"/>
            <property name="characterEncoding" value="UTF-8"/>
        </bean>
    
        <bean id="templateEngine" class="org.thymeleaf.spring5.SpringTemplateEngine">
            <property name="templateResolver" ref="templateResolver"></property>
            <property name="additionalDialects">
                <set>
                    <!--方言解释器-->
                    <bean class="at.pollux.thymeleaf.shiro.dialect.ShiroDialect"/>
                </set>
            </property>
        </bean>
    
        <bean id="viewResolver" class="org.thymeleaf.spring5.view.ThymeleafViewResolver">
            <property name="templateEngine" ref="templateEngine"/>
            <property name="characterEncoding" value="UTF-8"/>
        </bean>
    

## 这是pom.xml
    
    
     <!--Shiro-->
            <!--集成spring-->
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-spring</artifactId>
                <version>1.7.1</version>
            </dependency>
            <!--web项目-->
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-web</artifactId>
                <version>1.7.1</version>
            </dependency>
            <!--shiro日志-->
    
    
            <!-- shiro  -->
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-all</artifactId>
                <version>1.7.1</version>
            </dependency>
    
            <!-- 引入ehcache的依赖,给shiro做缓存权限用的 -->
            <dependency>
                <groupId>net.sf.ehcache</groupId>
                <artifactId>ehcache</artifactId>
                <version>2.10.6</version>
            </dependency>
    
    
    
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-core</artifactId>
                <version>1.4.1</version>
            </dependency>
    
            <!-- Shiro uses SLF4J for logging.  We'll use the 'simple' binding
                 in this example app.  See http://www.slf4j.org for more info. -->
            <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-simple</artifactId>
                <version>1.7.21</version>
                <scope>compile</scope>
            </dependency>
            <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>jcl-over-slf4j</artifactId>
                <version>1.7.21</version>
                <scope>compile</scope>
            </dependency>
    
            <dependency>
                <groupId>org.thymeleaf</groupId>
                <artifactId>thymeleaf</artifactId>
                <version>3.0.10.RELEASE</version>
            </dependency>
    
            <dependency>
                <groupId>org.thymeleaf</groupId>
                <artifactId>thymeleaf-spring5</artifactId>
                <version>3.0.10.RELEASE</version>
            </dependency>
    
            <dependency>
                <groupId>com.github.theborakompanioni</groupId>
                <artifactId>thymeleaf-extras-shiro</artifactId>
                <version>2.0.0</version>
            </dependency>
    
            <dependency>
                <groupId>org.attoparser</groupId>
                <artifactId>attoparser</artifactId>
                <version>2.0.0.RELEASE</version>
            </dependency>
    

## 以下是html
    
    
    <html lang="en" xmlns:th="http://www.thymeleaf.org"
          xmlns:shiro="http://www.pollix.at/thymeleaf/shiro">
    
    <head>
        <meta charset="UTF-8">
        <title>index</title>
    </head>
    <body>
    
    <h1>index</h1>
    <a  href="/logout">logout</a>
    <br><br>
    
    <a href="common.html">一般用户</a>
    <a href="admin.html">管理员</a>
    
    <p shiro:hasRole="admin">
    你好 管理员！
    </p>
    <a shiro:hasRole="user">你好user</a>
    <a href="/shiroTest">测试时间</a>
    
    
    </body>
    </html>
    

### 普通用户登录

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/25d27ecf3cb9b32aad9c85e84154198b.png)  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/73cbef562e28131bb9209714328b6828.png)

#### 显示你好user

=====================================

### 管理员登录、

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/80b9d7fd8146775e70a3a2e23563361d.png)  
显示你好管理员，
