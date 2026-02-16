---
title: "mysql: /usr/local/MATLAB/MATLAB_Runtime/v901/sys/os/glnxa64/libstdc++.so.6: version `CXXABI_1.3.9‘ n"
date: 2021-12-09
tags:
  - CSDN迁移
---

# mysql: /usr/local/MATLAB/MATLAB_Runtime/v901/sys/os/glnxa64/libstdc++.so.6: version `CXXABI_1.3.9‘ n

## 项目场景：

运行在centos中，执行mysql指令出错

> mysql: /usr/local/MATLAB/MATLAB_Runtime/v901/sys/os/glnxa64/libstdc++.so.6: version `CXXABI_1.3.9’ not found (required by mysql) centos

## 问题描述：

执行终端mysql命令出错

## 原因分析：

matlab中的libstdc++与系统自带的冲突。

## 解决方案：

删除其中一个就可以  
1.  
查看系统所有关于 'libstdc++.so.6’的文件路径
    
    
    [root@wanhua ~]# find / -name 'libstdc++.so.6'
    /usr/lib64/libstdc++.so.6
    /usr/local/MATLAB
