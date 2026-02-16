---
title: "Vue 父组件传值子组件无效"
date: 2023-02-03
description: "vue子组件接收数据无效，生命周期问题（已解决）"
tags:
  - CSDN迁移
---

# Vue 父组件传值子组件无效

## 项目场景：

`背景：`

在父组件mounted钩子中，获取接口数据。然后，通过props 传递给子组件。

* * *

## 问题描述

`遇到的问题：`

子组件mounted接收数据无效。

* * *

## 原因分析：

> 分析：

在父组件获取api数据以后，传递给子组件，由于发起的请求是个异步函数，不能保证子组件挂载时数据获取完成。

* * *

## 解决方案：

> 方案：使用v-if保证在子组件挂载完成后，数据可以获取到。v-if=“传递的数据是否存在”
    
    
     <pagination v-if="alllist.length!==0" @GetList="GetList" :list='alllist' />
