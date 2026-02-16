---
title: "fgets()，strtod(),strnlen(),strcmp()函数记录"
date: 2020-02-10
tags:
  - CSDN迁移
---

# fgets()，strtod(),strnlen(),strcmp()函数记录

#include `&lt;stdio.h&gt;`  
#include `&lt;stdbool.h&gt;`  
#include `&lt;stdlib.h&gt;`  
#include `&lt;math.h&gt;`  
#include `&lt;ctype.h&gt;`  
#include `&lt;string.h&gt;`  
#define buf_len 256  
#define **STDC_WANT_LIB_EXT1** 1  
int main(){  
char *ptr=NULL;  
char buf[buf_len];  
size_t to=0;  
size_t buf_lenth=0;  
size_t index=0;  
double result=0.0;  
double number=0.0;  
char *endptr=NULL;  
char op=0;  
while(true){  
ptr=fgets(buf,buf_len,stdin);  
if(!ptr){  
printf(“error reading input\n”);
    
    
    	}
    	if(strcmp(buf,"quit\n")==0){
    		break;
    	}
    	buf_lenth=strnlen(buf,buf_len);
    	buf[--buf_lenth]='\0';
    	for (to =0,index=0;index<=buf_lenth;++index){
    		if(*(buf+index)!=' '){
    			*(buf+to++)=*(buf+index);
    		}
    	}
    	index=0;
    	if(buf[index]=='=')index++;
    	else{
    		result=strtod(buf+index,&endptr); 
    		index=endptr-buf;
    	}
    	while(index<buf_lenth){
    		op=*(buf+index++);
    		number=strtod(buf+index,&endptr);
    		index=endptr-buf;//获取下一个字符的索引
    		switch(op){
    			case'+':result+=number;break;
    			case'-':result-=number;break;
    			case'*':result*=number;break;
    			case'/':
    			if(number==0){
    				printf("error 0 ");
    			}
    			else {
    			result/=number;}
    			break;
    			case'%':
    		if((long long)number==0LL){
    			printf("分母不能为零"); 
    		}
    		 else 
    		 {
    		 result=(double)((long long)result%(long long)number);break;
    	}
    		default:printf("inigall 操作失败\n");break;
    		} 
    	/*	if(strcmp(buf,"\n")==0){
    		printf("= %f",result);
    		}*/
    	
    	}
    		printf("= %f\n",result); 	
    }
    
    return 0;
    

}
