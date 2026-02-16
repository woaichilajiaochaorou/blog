---
title: "实现strcta函数"
date: 2020-03-11
description: "实现strcat函数#include <stdio.h>#include <string.h>#define MAXS 10char *str_cat( char *s, char *t ){	int i=0;	int j=0;	for(i=strlen(s);i<(strlen(s)+strlen(t));i++){				s[i]=t[j]..."
tags:
  - CSDN迁移
---

# 实现strcta函数

**实现strcat函数**
    
    
    #include <stdio.h>
    #include <string.h>
    
    #define MAXS 10
    
    char *str_cat( char *s, char *t ){
    	int i=0;
    	int j=0;
    	for(i=strlen(s);i<(strlen(s)+strlen(t));i++){
    		
    		s[i]=t[j];
    		++j;		
    	}
    	s[i+1]='\0';
    	return  s;
    }
    
    int main()
    {
        char *p;
        char str1[MAXS+MAXS] = {'\0'}, str2[MAXS] = {'\0'};
    
        scanf("%s%s", str1, str2);
        p = str_cat(str1, str2);
        printf("%s\n%s\n", p, str1);
    
        return 0;
    }
