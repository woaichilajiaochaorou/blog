---
title: "spring web 整合shiro"
date: 2021-05-31
tags:
  - CSDN迁移
---

# spring web 整合shiro

**话不多说直接上步骤：**  
第一步，导入依赖。
    
    
            <!--Shiro-->
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-core&lt;/artifactId&gt;
                &lt;version&gt;1.4.1&lt;/version&gt;
            &lt;/dependency&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-ehcache&lt;/artifactId&gt;
                &lt;version&gt;1.2.2&lt;/version&gt;
            &lt;/dependency&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-quartz&lt;/artifactId&gt;
                &lt;version&gt;1.2.2&lt;/version&gt;
            &lt;/dependency&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-spring&lt;/artifactId&gt;
                &lt;version&gt;1.2.2&lt;/version&gt;
            &lt;/dependency&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.apache.shiro&lt;/groupId&gt;
                &lt;artifactId&gt;shiro-web&lt;/artifactId&gt;
                &lt;version&gt;1.7.1&lt;/version&gt;
            &lt;/dependency&gt;
            
            <!-- Shiro uses SLF4J for logging.  We'll use the 'simple' binding
                 in this example app.  See http://www.slf4j.org for more info. -->
            &lt;dependency&gt;
                &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
                &lt;artifactId&gt;slf4j-simple&lt;/artifactId&gt;
                &lt;version&gt;1.7.21&lt;/version&gt;
                &lt;scope&gt;test&lt;/scope&gt;
            &lt;/dependency&gt;
            &lt;dependency&gt;
                &lt;groupId&gt;org.slf4j&lt;/groupId&gt;
                &lt;artifactId&gt;jcl-over-slf4j&lt;/artifactId&gt;
                &lt;version&gt;1.7.21&lt;/version&gt;
                &lt;scope&gt;test&lt;/scope&gt;
            &lt;/dependency&gt;
            
            <!--shiro使用ehcache-->
            &lt;dependency&gt;
                &lt;groupId&gt;net.sf.ehcache&lt;/groupId&gt;
                &lt;artifactId&gt;ehcache&lt;/artifactId&gt;
                &lt;version&gt;2.10.2&lt;/version&gt;
            &lt;/dependency&gt;                           
    
           <!--shiro 支持html-->
            &lt;dependency&gt;
                &lt;groupId&gt;com.github.theborakompanioni&lt;/groupId&gt;
                &lt;artifactId&gt;thymeleaf-extras-shiro&lt;/artifactId&gt;
                &lt;version&gt;2.0.0&lt;/version&gt;
            &lt;/dependency&gt;
    
    

第二步配置spring-shiro.xml
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    &lt;beans xmlns="http://www.springframework.org/schema/beans"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.springframework.org/schema/beans
    			http://www.springframework.org/schema/beans/spring-beans-4.0.xsd"&gt;
    
    
        <!--1.配置securityManager-->
        <!--2.配置shiro缓存ehcache-->
        <!--3.配置realm-->
        <!--4.配置生命周期处理器-->
        &lt;bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager"&gt;
            <!-- Single realm app.  If you have multiple realms, use the 'realms' property instead. -->
            &lt;property name="realm" ref="myRealm" /&gt;
            &lt;property name="cacheManager" ref="cacheManager"&gt;&lt;/property&gt;
            <!-- By default the servlet container sessions will be used.  Uncomment this line
                 to use shiro's native sessions (see the JavaDoc for more): -->
            <!-- &lt;property name="sessionMode" value="native"/&gt; -->
        &lt;/bean&gt;
        &lt;bean name="cacheManager" class="org.apache.shiro.cache.ehcache.EhCacheManager" &gt;
            &lt;property name="cacheManagerConfigFile" value="classpath:shiro/ehcache.xml"&gt;&lt;/property&gt;
        &lt;/bean&gt;
    
        <!-- Define the Shiro Realm implementation you want to use to connect to your back-end -->
        <!-- security datasource: -->
        <!--这里用了自定义的realm-->
        &lt;bean id="myRealm" class="myrealm"&gt;&lt;/bean&gt;
    
        <!--可以自动地调用spring ioc 容器中的生命周期方法-->
        &lt;bean id="lifecycleBeanPostProcessor" class="org.apache.shiro.spring.LifecycleBeanPostProcessor"/&gt;
    
        <!--允许在ioc容器中使用shiro注解 只有配置生命周期处理器之后在可以使用 -->
        <!-- Enable Shiro Annotations for Spring-configured beans.  Only run after -->
        <!-- the lifecycleBeanProcessor has run: -->
        &lt;bean class="org.springframework.aop.framework.autoproxy.DefaultAdvisorAutoProxyCreator" depends-on="lifecycleBeanPostProcessor"/&gt;
        &lt;bean class="org.apache.shiro.spring.security.interceptor.AuthorizationAttributeSourceAdvisor"&gt;
            &lt;property name="securityManager" ref="securityManager"/&gt;
        &lt;/bean&gt;
        <!--配置shirofilter 其中id 必须和web.xml文件中的filtername一致   -->
        &lt;bean id="shiroFilter" class="org.apache.shiro.spring.web.ShiroFilterFactoryBean"&gt;
            &lt;property name="securityManager" ref="securityManager"/&gt;
            &lt;property name="loginUrl" value="/login.html"/&gt;<!--默认访问页面-->
            &lt;property name="successUrl" value="/index.html"/&gt;
            &lt;property name="unauthorizedUrl" value="/unauthorized.html"/&gt;
            <!-- The 'filters' property is not necessary since any declared javax.servlet.Filter bean  -->
            <!-- defined will be automatically acquired and available via its beanName in chain        -->
            <!-- definitions, but you can perform instance overrides or name aliases here if you like: -->
            <!-- &lt;property name="filters"&gt;
                &lt;util:map&gt;
                    &lt;entry key="logout" value-ref="logoutFilter" /&gt;
                &lt;/util:map&gt;
            &lt;/property&gt; -->
            <!--配置哪些页面需要受保护 以及访问页面所需要的权限是什么-->
            &lt;property name="filterChainDefinitions"&gt;
                &lt;value&gt;
                    <!-- # some example chain definitions:
                     # /admin/** = authc, roles[admin]
                     # /docs/** = authc, perms[document:read]
                  -->
                    /index.html=anon
                    /login.html=authc
                    /** = anon
                    <!-- # more URL-to-FilterChain definitions here-->
                &lt;/value&gt;
            &lt;/property&gt;
        &lt;/bean&gt;
    &lt;/beans&gt;
    
    

第三步配置web.xml
    
    
    在这里插入代码片<?xml version="1.0" encoding="UTF-8"?>
    &lt;web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
             version="4.0"&gt;
        &lt;servlet&gt;
            &lt;servlet-name&gt;SpringMVC&lt;/servlet-name&gt;
            &lt;servlet-class&gt;org.springframework.web.servlet.DispatcherServlet&lt;/servlet-class&gt;
            &lt;init-param&gt;
                &lt;param-name&gt;contextConfigLocation&lt;/param-name&gt;
                &lt;param-value&gt;
                    classpath:spring/spring.xml
                    classpath:shiro/spring-shiro.xml
                &lt;/param-value&gt;
            &lt;/init-param&gt;
            &lt;load-on-startup&gt;1&lt;/load-on-startup&gt;
        &lt;/servlet&gt;
        &lt;servlet-mapping&gt;
            &lt;servlet-name&gt;SpringMVC&lt;/servlet-name&gt;
            &lt;url-pattern&gt;/&lt;/url-pattern&gt;
        &lt;/servlet-mapping&gt;
    
    
    
        <!-- shiro filter start 集成mvc-->
        &lt;filter&gt;
            &lt;filter-name&gt;shiroFilter&lt;/filter-name&gt;
            &lt;filter-class&gt;
                org.springframework.web.filter.DelegatingFilterProxy
            &lt;/filter-class&gt;
            &lt;init-param&gt;
                &lt;param-name&gt;targetFilterLifecycle&lt;/param-name&gt;
                &lt;param-value&gt;true&lt;/param-value&gt;
            &lt;/init-param&gt;
        &lt;/filter&gt;
        &lt;filter-mapping&gt;
            &lt;filter-name&gt;shiroFilter&lt;/filter-name&gt;
            &lt;url-pattern&gt;/*&lt;/url-pattern&gt;
        &lt;/filter-mapping&gt;
        <!-- shiro filter end -->
    &lt;/web-app&gt;
    

**启动项目**
