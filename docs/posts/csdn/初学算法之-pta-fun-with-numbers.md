---
title: "初学算法之---pta fun with numbers"
date: 2021-07-16
description: "#include<stdio.h>	#include<math.h>	#include<string.h>	 int main(){	char a[21];	char b[21]={0};	scanf('%s',&a);		int len=strlen(a);	/*	for(int i=0;i<len;i++){		array[i]	}	*/	//统计数字出现次数 下标就是数字 	int num1"
tags:
  - CSDN迁移
---

# 初学算法之---pta fun with numbers

#include<stdio.h>
    	#include<math.h>
    	#include<string.h>
    	 
    int main(){
    	char a[21];
    	char b[21]={0};
    	scanf("%s",&a);
    		int len=strlen(a);
    	/*
    
    	for(int i=0;i<len;i++){
    		array[i]
    	}
    	*/
    	//统计数字出现次数 下标就是数字 
    	int num1[10] = {0};
    	for(int i=0;i<len;i++){
    		int j=a[i]-'0';
    		num1[j]++;
    	}
    
    	int index=len;
    	for(int j=len;j>0;j--){	
    		int nums=(a[index-1]-'0')*2;
    		if(nums>=10){//产生进位 
    			b[j]+=nums%10 ;
    			b[j-1]+=nums/10;
    		}else{
    			b[j]+=nums;
    		}
    		index--;
    	}
    	
    	//计算b数组的数字种类
    	 int num2[10] = {0};
    	for(int i=0;i<len;i++){
    		//printf("%d ",b[i+1]);
    		int j=b[i+1];
    		num2[j]++;
    	}
    
    
    	
    	 
    	/*如果发生多出一位则no*/
    	if(b[0]!=0){
    		printf("No\n");
    		for(int j=0;j<=len;j++){
    			printf("%d",b[j]);
    		}
    		return 0;
    	}
    	
    	//比较ab 是否数字种类不一致
    	int round;
    	if(len>9){
    		round=10;
    	}
    	for(int i=0;i<round;i++){
    		if(num1[i]==0&&num2[i]!=0){
    			printf("No\n");
    			for(int j=1;j<=len;j++){
    			printf("%d",b[j]);
    		}
    		return 0;	
    	}
    	if(num1[i]!=0&&num2[i]==0){
    			printf("No\n");
    			for(int j=1;j<=len;j++){
    			printf("%d",b[j]);
    		}
    		return 0;	
    	}
    } 
    	
    	//满足条件yes 
    	printf("Yes\n");
    	for(int j=1;j<=len;j++){
    			printf("%d",b[j]);
    	}
    }
