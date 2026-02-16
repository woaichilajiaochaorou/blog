---
title: "Spring 6.2.2 @scope(“prototype“)原理"
date: 2025-02-08
description: "spring scope prototype 原理"
tags:
  - CSDN迁移
---

# Spring 6.2.2 @scope(“prototype“)原理

### Spring @Prototype 原理？

#### 前置准备

  1. 创建一个MyService类

    
    
    @Scope("prototype")
    @Service("myService")
    public class MyService {
        public String getMessage() {
            return "Hello, World!";
        }
    }
    

  2. 创建一个main类，用于debug。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/97bc85f7559a4683890d92c9df878a37.png)

#### prototype 如何生效？

在`context.getBean();`方法中，有一个核心方法`doGetBean()`
    
    
    protected <T> T doGetBean(
    			String name, @Nullable Class<T> requiredType, @Nullable Object[] args, boolean typeCheckOnly)
    			throws BeansException {
    			......省略
    			try {
    				// Create bean instance.
    				if (mbd.isSingleton()) {
    					sharedInstance = getSingleton(beanName, () -> {
    						try {
    							return createBean(beanName, mbd, args);
    						}
    						catch (BeansException ex) {
    							// Explicitly remove instance from singleton cache: It might have been put there
    							// eagerly by the creation process, to allow for circular reference resolution.
    							// Also remove any beans that received a temporary reference to the bean.
    							destroySingleton(beanName);
    							throw ex;
    						}
    					});
    					beanInstance = getObjectForBeanInstance(sharedInstance, name, beanName, mbd);
    				}
    
    				else if (mbd.isPrototype()) {
    					// It's a prototype -> create a new instance.
    					Object prototypeInstance = null;
    					try {
    						beforePrototypeCreation(beanName);
    						prototypeInstance = createBean(beanName, mbd, args);
    					}
    					finally {
    						afterPrototypeCreation(beanName);
    					}
    					beanInstance = getObjectForBeanInstance(prototypeInstance, name, beanName, mbd);
    				}
    
    				....省略
    
    		return adaptBeanInstance(name, beanInstance, requiredType);
    	}
    

存在一个判断：`else if (mbd.isPrototype())` 当`bean definition`的`scope`为`prototype`的时候调用`createBean()`将创建一个新的`bean`。
