---
title: "c语言进制转换 栈的操作"
date: 2020-03-25
tags:
  - CSDN迁移
---

# c语言进制转换 栈的操作

#include `&lt;stdio.h&gt;`  
    #include `&lt;string.h&gt;`  
    #include `&lt;stdlib.h&gt;` 
    #include `&lt;math.h&gt;` 
    #include `&lt;windows.h&gt;`
    #define maxsize 20
    #define Elemtype char  
    typedef struct {
    	Elemtype *top;
    	Elemtype *bottom;
    	int stack_size;
    }stack;
    void initial_stack(stack *s){
    	s->bottom=(Elemtype*)malloc(maxsize*sizeof(Elemtype));
    	if(!s->bottom){
    		printf("error");
    		exit(-1);
    	}
    	s->top=s->bottom;
    	s->stack_size=maxsize;	 
    } 
    void push(stack *s,Elemtype *e){
    	if(s->top-s->bottom>=s->stack_size){
    		s->stack_size+=maxsize;
    		s->bottom=(Elemtype *)realloc(s->bottom,(s->stack_size+maxsize));
    	}
    	if(!s->bottom){
    		exit(0);
    	}
    	*(s->top)=*e;
    	s->top++;
    }
    void pop(stack *s,Elemtype *e){
    	if(s->top==s->bottom){
    		printf("栈空！\n");
    	}
    	else
    	{
    		*e=*--(s->top);
    	}
    	
    }
    int stack_len(stack s){
    	return (s.top-s.bottom); 
    }
    
    int main(){
    	stack s;
    	Elemtype c;
    	int len,i;
    	int sum=0;
    	printf("请输入二进制数\n");
    	initial_stack(&s);
    	scanf("%c",&c);
    	while(c!='#'){
    		push(&s,&c);
    		scanf("%c",&c);
    	}
    	getchar();//去掉回车 
    	len=stack_len(s);
    	printf("\n栈的当前容量是%d\n",len);
    	for(i=0;i<len;i++){
    		pop(&s,&c);
    		sum=sum+(c-48)*pow(2,i);
    	}
    	printf("\n二进制数转化为十进制:%d",sum);
    	return 0;
    }
