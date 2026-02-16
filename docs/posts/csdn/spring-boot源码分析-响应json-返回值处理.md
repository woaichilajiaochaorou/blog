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

## 3，![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/29a3d3024ecf79ca819ed3efb2aa2e61.png)

执行完这个方法后，得到返回值，进行一些返回值安全判断后。

## 4，使用返回值处理器进行处理。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/956aaf45ce48670cd9bd15b8fac656fa.png)

#### 下面分析这个方法怎么处理：

1.首先调用了这个方法：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2d516639a5c5af39dc3262d6965acda3.png)  
stepover --》stepinto  
2.来到真正的处理方法中：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/91eee693a7a75bd184de295b0aa2ea7a.png)  
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
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b6634c9dbdf47c54a3ac98552e8d0696.png)  
找到对应处理器后执行该方法：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b89f7c6c785a7087c6aa490bc43bea75.png)  
步入：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4fddf6e9ec68aff594359fd85c7eeb76.png)

使用消息转换器进行写出操作。步入该方法-》

首先对返回值的类型进行一系列判断，  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0aaee10b706c11b3a73941f5deb51b6b.png)  
都不是则需要判断媒体类型，与浏览器进行内容协商  
获得浏览器支持显示的内容类型  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4cc932541b374a9f3a2aaad26d6bc178.png)

##### 有如下7种:

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/339a3cfaabc58730e18150cacd07438a.png)

##### 进行协商，将能用的mediaType放入List

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/355cd389aea2f8a14a9c85e94cb61b0d.png)

##### 确定使用的类型为json

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9607c0d0afc4af03dfe105e642737851.png)

##### 遍历所有messageConverter

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a391a39c1df6ec6a82307c1dfc26273e.png)  
这是所有converter：  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ade0d57614aa12c2ae9c8d5da0ca9c6f.png)  
每种messageConverter支持的返回值类型都不一样。  
最终无论你是什么类型遇到最后一种直接转为json  
调用objectWriter  
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/42f257b2621d0f4781dec307ca895223.png)
