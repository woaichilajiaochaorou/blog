---
title: "java.lang.UnsatisfiedLinkError: org.opencv.core.Mat.n_Mat(IIILjava/nio/ByteBuffer；)J [duplicate]"
date: 2021-11-13
tags:
  - CSDN迁移
---

# java.lang.UnsatisfiedLinkError: org.opencv.core.Mat.n_Mat(IIILjava/nio/ByteBuffer；)J [duplicate]

**java.lang.UnsatisfiedLinkError: org.opencv.core.Mat.n_Mat(IIILjava/nio/ByteBuffer;)J [duplicate]**

如果你只用maven导入了的话 可以在程序前面加上 以下代码：
    
    
    Loader.load(opencv_java.class)
