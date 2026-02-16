---
title: "shiro多重realm 及其认证策略"
date: 2021-06-04
tags:
  - CSDN迁移
---

# shiro多重realm 及其认证策略

**在shiro-spring.xml文件中，按以下配置:**
    
    
       <!--多重realm-->
        &lt;bean id="authenticator" class="org.apache.shiro.authc.pam.ModularRealmAuthenticator"&gt;
            <property name
