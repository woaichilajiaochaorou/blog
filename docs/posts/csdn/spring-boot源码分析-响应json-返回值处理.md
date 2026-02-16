---
title: "spring-boot源码分析--响应json 返回值处理"
date: 2021-08-23
tags:
  - CSDN迁移
---

# spring-boot源码分析--响应json 返回值处理

## 1，spring-boot 引入web包后带有json的stater。
    
    
    只需在类方法上面responseBody就可以。
    

## 2，有返回值解析器returnValueHandlers进行处理。

## 3，![在这里插入图片描述](/images/csdn/5db3effa3ad3.png)

执行完这个方法后，得到返回值，进行一些返回值安全判断后。

## 4，使用返回值处理器进行处理。

![在这里插入图片描述](/images/csdn/0231f1b6ee22.png)

#### 下面分析这个方法怎么处理：

1.首先调用了这个方法：  
![在这里插入图片描述](/images/csdn/c641ca1618e0.png)  
stepover --》stepinto  
2.来到真正的处理方法中：  
![在这里插入图片描述](/images/csdn/6b09e88bd504.png)  
首先，选择一个对应的handler  
返回值处理器会判断返回值处理器是否支持处理该类型返回值，支持就处理。  
拓展：根据supportsReturnType 查看到返回值支持以下类型
    
    
    view
    ResponseEntity
    StreamingResponseBody
    HttpEntity
    HttpHeaders
    Callable
    DeferredResult
    ListenableFuture
    CompletionStage
    WebAsyncTask
    hasMethodAnnotation(ModelAttribute.class) 被此注解标注的方法也可以被处理
    被ResponseBody.class标注的方法返回值可被处理
    etc.....
    

被@ResponseBody标注的被次处理器处理 （requestresponsebodymethodprocessor）  
![在这里插入图片描述](/images/csdn/2b3222401b8c.png)  
找到对应处理器后执行该方法：  
![在这里插入图片描述](/images/csdn/28b6073cb1ef.png)  
步入：  
![在这里插入图片描述](/images/csdn/e55a551c4c49.png)

使用消息转换器进行写出操作。步入该方法-》

首先对返回值的类型进行一系列判断，  
![在这里插入图片描述](/images/csdn/f74e1cf596c5.png)  
都不是则需要判断媒体类型，与浏览器进行内容协商  
获得浏览器支持显示的内容类型  
![在这里插入图片描述](/images/csdn/40d20b94aac3.png)

##### 有如下7种:

![在这里插入图片描述](/images/csdn/b21fc917b74a.png)

##### 进行协商，将能用的mediaType放入List

![在这里插入图片描述](/images/csdn/492b9b4c57ef.png)

##### 确定使用的类型为json

![在这里插入图片描述](/images/csdn/08d94b73055f.png)

##### 遍历所有messageConverter

![在这里插入图片描述](/images/csdn/c04691f088ef.png)  
这是所有converter：  
![在这里插入图片描述](/images/csdn/8d403bd61112.png)  
每种messageConverter支持的返回值类型都不一样。  
最终无论你是什么类型遇到最后一种直接转为json  
调用objectWriter  
![在这里插入图片描述](/images/csdn/2b203c8dc86a.png)
