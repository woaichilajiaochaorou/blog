---
title: "spring web 整合shiro"
date: 2021-05-31
description: "话不多说直接上步骤：第一步，导入依赖。        <!--Shiro-->        <dependency>            <groupId>org.apache.shiro</groupId>            <artifactId>shiro-core</artifactId>            <version>1.4.1</version>        &lt"
tags:
  - CSDN迁移
---

# spring web 整合shiro

**话不多说直接上步骤：**  
第一步，导入依赖。
    
    
            <!--Shiro-->
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-core</artifactId>
                <version>1.4.1</version>
            </dependency>
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-ehcache</artifactId>
                <version>1.2.2</version>
            </dependency>
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-quartz</artifactId>
                <version>1.2.2</version>
            </dependency>
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-spring</artifactId>
                <version>1.2.2</version>
            </dependency>
            <dependency>
                <groupId>org.apache.shiro</groupId>
                <artifactId>shiro-web</artifactId>
                <version>1.7.1</version>
            </dependency>
            
            <!-- Shiro uses SLF4J for logging.  We'll use the 'simple' binding
                 in this example app.  See http://www.slf4j.org for more info. -->
            <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>slf4j-simple</artifactId>
                <version>1.7.21</version>
                <scope>test</scope>
            </dependency>
            <dependency>
                <groupId>org.slf4j</groupId>
                <artifactId>jcl-over-slf4j</artifactId>
                <version>1.7.21</version>
                <scope>test</scope>
            </dependency>
            
            <!--shiro使用ehcache-->
            <dependency>
                <groupId>net.sf.ehcache</groupId>
                <artifactId>ehcache</artifactId>
                <version>2.10.2</version>
            </dependency>                           
    
           <!--shiro 支持html-->
            <dependency>
                <groupId>com.github.theborakompanioni</groupId>
                <artifactId>thymeleaf-extras-shiro</artifactId>
                <version>2.0.0</version>
            </dependency>
    
    

第二步配置spring-shiro.xml
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
           xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:schemaLocation="http://www.springframework.org/schema/beans
    			http://www.springframework.org/schema/beans/spring-beans-4.0.xsd">
    
    
        <!--1.配置securityManager-->
        <!--2.配置shiro缓存ehcache-->
        <!--3.配置realm-->
        <!--4.配置生命周期处理器-->
        <bean id="securityManager" class="org.apache.shiro.web.mgt.DefaultWebSecurityManager">
            <!-- Single realm app.  If you have multiple realms, use the 'realms' property instead. -->
            <property name="realm" ref="myRealm" />
            <property name="cacheManager" ref="cacheManager"></property>
            <!-- By default the servlet container sessions will be used.  Uncomment this line
                 to use shiro's native sessions (see the JavaDoc for more): -->
            <!-- <property name="sessionMode" value="native"/> -->
        </bean>
        <bean name="cacheManager" class="org.apache.shiro.cache.ehcache.EhCacheManager" >
            <property name="cacheManagerConfigFile" value="classpath:shiro/ehcache.xml"></property>
        </bean>
    
        <!-- Define the Shiro Realm implementation you want to use to connect to your back-end -->
        <!-- security datasource: -->
        <!--这里用了自定义的realm-->
        <bean id="myRealm" class="myrealm"></bean>
    
        <!--可以自动地调用spring ioc 容器中的生命周期方法-->
        <bean id="lifecycleBeanPostProcessor" class="org.apache.shiro.spring.LifecycleBeanPostProcessor"/>
    
        <!--允许在ioc容器中使用shiro注解 只有配置生命周期处理器之后在可以使用 -->
        <!-- Enable Shiro Annotations for Spring-configured beans.  Only run after -->
        <!-- the lifecycleBeanProcessor has run: -->
        <bean class="org.springframework.aop.framework.autoproxy.DefaultAdvisorAutoProxyCreator" depends-on="lifecycleBeanPostProcessor"/>
        <bean class="org.apache.shiro.spring.security.interceptor.AuthorizationAttributeSourceAdvisor">
            <property name="securityManager" ref="securityManager"/>
        </bean>
        <!--配置shirofilter 其中id 必须和web.xml文件中的filtername一致   -->
        <bean id="shiroFilter" class="org.apache.shiro.spring.web.ShiroFilterFactoryBean">
            <property name="securityManager" ref="securityManager"/>
            <property name="loginUrl" value="/login.html"/><!--默认访问页面-->
            <property name="successUrl" value="/index.html"/>
            <property name="unauthorizedUrl" value="/unauthorized.html"/>
            <!-- The 'filters' property is not necessary since any declared javax.servlet.Filter bean  -->
            <!-- defined will be automatically acquired and available via its beanName in chain        -->
            <!-- definitions, but you can perform instance overrides or name aliases here if you like: -->
            <!-- <property name="filters">
                <util:map>
                    <entry key="logout" value-ref="logoutFilter" />
                </util:map>
            </property> -->
            <!--配置哪些页面需要受保护 以及访问页面所需要的权限是什么-->
            <property name="filterChainDefinitions">
                <value>
                    <!-- # some example chain definitions:
                     # /admin/** = authc, roles[admin]
                     # /docs/** = authc, perms[document:read]
                  -->
                    /index.html=anon
                    /login.html=authc
                    /** = anon
                    <!-- # more URL-to-FilterChain definitions here-->
                </value>
            </property>
        </bean>
    </beans>
    
    

第三步配置web.xml
    
    
    在这里插入代码片<?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
             version="4.0">
        <servlet>
            <servlet-name>SpringMVC</servlet-name>
            <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
            <init-param>
                <param-name>contextConfigLocation</param-name>
                <param-value>
                    classpath:spring/spring.xml
                    classpath:shiro/spring-shiro.xml
                </param-value>
            </init-param>
            <load-on-startup>1</load-on-startup>
        </servlet>
        <servlet-mapping>
            <servlet-name>SpringMVC</servlet-name>
            <url-pattern>/</url-pattern>
        </servlet-mapping>
    
    
    
        <!-- shiro filter start 集成mvc-->
        <filter>
            <filter-name>shiroFilter</filter-name>
            <filter-class>
                org.springframework.web.filter.DelegatingFilterProxy
            </filter-class>
            <init-param>
                <param-name>targetFilterLifecycle</param-name>
                <param-value>true</param-value>
            </init-param>
        </filter>
        <filter-mapping>
            <filter-name>shiroFilter</filter-name>
            <url-pattern>/*</url-pattern>
        </filter-mapping>
        <!-- shiro filter end -->
    </web-app>
    

**启动项目**
