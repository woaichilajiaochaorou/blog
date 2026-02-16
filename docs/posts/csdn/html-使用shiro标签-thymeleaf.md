---
title: "html 使用shiro标签 thymeleaf"
date: 2021-06-13
tags:
  - CSDN迁移
---

# html 使用shiro标签 thymeleaf

## 这是spring.xml的配置文件，
    
    
    <!--使用thyme leaf-->
        <!--视图解析器-->
        &lt;bean id="templateResolver" class="org.thymeleaf.spring5.templateresolver.SpringResourceTemplateResolver"&gt;
            &lt;property name="prefix" value="/"&gt;&lt;/property&gt;
            &lt;property name="suffix" value=".html"&gt;&lt;/property&gt;
            &lt;property name="templateMode" value="HTML"&gt;&lt;/property&gt;
            &lt;property name="cacheable" value="false"/&gt;
            &lt;property name="characterEncoding" value="UTF-8"/&gt;
        &lt;/bean&gt;
    
        &lt;bean id="templateEngine" class="org.thymeleaf.spring5.SpringTemplateEngine"&gt;
            &lt;property name="templateResolver" ref="templateResolver"&gt;&lt;/property&gt;
            &lt;property name="additionalDialects"&gt;
                &lt;set&gt;
                    <!--方言解释器-->
                    &lt;bean class="at.pollux.thymeleaf.shiro.dialect.ShiroDialect"/&gt;
                &lt;/set&gt;
            &lt;/property&gt;
        &lt;/bean&gt;
    
        &lt;bean id="viewResolver" class="org.thymeleaf.spring5.view.ThymeleafViewResolver"&gt;
            &lt;property name="templateEngine" ref="templateEngine"/&gt;
            &lt;property name="characterEncoding" value="UTF-8"/&gt;
        &lt;/bean&gt;
    

## 这是pom.xml
    
    
     <!--Shiro-->
            <!--集成spring-->
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-spring&lt;/artifactId&gt;
                &lt;version&gt;1.7.1&lt;/version&gt;
            &lt;/dependency&gt;
            <!--web项目-->
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-web&lt;/artifactId&gt;
                &lt;version&gt;1.7.1&lt;/version&gt;
            &lt;/dependency&gt;
            <!--shiro日志-->
    
    
            <!-- shiro  -->
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-all&lt;/artifactId&gt;
                &lt;version&gt;1.7.1&lt;/version&gt;
            &lt;/dependency&gt;
    
            <!-- 引入ehcache的依赖,给shiro做缓存权限用的 -->
            &lt;dependency&gt;
                &lt;groupId&gt;net.sf.ehcache&lt;/groupId&gt;
                &lt;artifactId&gt;ehcache&lt;/artifactId&gt;
                &lt;version&gt;2.10.6&lt;/version&gt;
            &lt;/dependency&gt;
    
    
    
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-core&lt;/artifactId&gt;
                &lt;version&gt;1.4.1&lt;/version&gt;
            &lt;/dependency&gt;
    
            <!-- Shiro uses SLF4J for logging.  We'll use the 'simple' binding
                 in this example app.  See http://www.slf4j.org for more info. -->
            &lt;dependency&gt;
                &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
                &lt;artifactId&gt;slf4j-simple&lt;/artifactId&gt;
                &lt;version&gt;1.7.21&lt;/version&gt;
                &lt;scope&gt;compile&lt;/scope&gt;
            &lt;/dependency&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
                &lt;artifactId&gt;jcl-over-slf4j&lt;/artifactId&gt;
                &lt;version&gt;1.7.21&lt;/version&gt;
                &lt;scope&gt;compile&lt;/scope&gt;
            &lt;/dependency&gt;
    
            &lt;dependency&gt;
                &lt;groupId&gt;org.thymeleaf&lt;/groupId&gt;
                &lt;artifactId&gt;thymeleaf&lt;/artifactId&gt;
                &lt;version&gt;3.0.10.RELEASE&lt;/version&gt;
            &lt;/dependency&gt;
    
            &lt;dependency&gt;
                &lt;groupId&gt;org.thymeleaf&lt;/groupId&gt;
                &lt;artifactId&gt;thymeleaf-spring5&lt;/artifactId&gt;
                &lt;version&gt;3.0.10.RELEASE&lt;/version&gt;
            &lt;/dependency&gt;
    
            &lt;dependency&gt;
                &lt;groupId&gt;com.github.theborakompanioni&lt;/groupId&gt;
                &lt;artifactId&gt;thymeleaf-extras-shiro&lt;/artifactId&gt;
                &lt;version&gt;2.0.0&lt;/version&gt;
            &lt;/dependency&gt;
    
            &lt;dependency&gt;
                &lt;groupId&gt;org.attoparser&lt;/groupId&gt;
                &lt;artifactId&gt;attoparser&lt;/artifactId&gt;
                &lt;version&gt;2.0.0.RELEASE&lt;/version&gt;
            &lt;/dependency&gt;
    

## 以下是html
    
    
    &lt;html lang="en" xmlns:th="http://www.thymeleaf.org"
          xmlns:shiro="http://www.pollix.at/thymeleaf/shiro"&gt;
    
    &lt;head&gt;
        &lt;meta charset="UTF-8"&gt;
        &lt;title&gt;index&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
    
    <h1>index&lt;/h1&gt;
    <a  href="/logout">logout&lt;/a&gt;
    <br><br>
    
    <a href="common.html">一般用户&lt;/a&gt;
    <a href="admin.html">管理员&lt;/a&gt;
    
    <p shiro:hasRole="admin">
    你好 管理员！
    &lt;/p&gt;
    <a shiro:hasRole="user">你好user&lt;/a&gt;
    <a href="/shiroTest">测试时间&lt;/a&gt;
    
    
    &lt;/body&gt;
    &lt;/html&gt;
    

### 普通用户登录

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/25d27ecf3cb9b32aad9c85e84154198b.png)  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/73cbef562e28131bb9209714328b6828.png)

#### 显示你好user

=====================================

### 管理员登录、

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/80b9d7fd8146775e70a3a2e23563361d.png)  
显示你好管理员，
