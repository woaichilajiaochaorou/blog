---
title: "Simon记忆游戏"
date: 2020-01-20
description: "这是我的一个小游戏simon#include <stdio.h>#include <ctype.h>#include <stdbool.h>#include <stdlib.h>#include <time.h>int main(){//初始化程序char another_game = 'N';bool correct ..."
tags:
  - CSDN迁移
---

# Simon记忆游戏

#include <stdio.h>
    #include <ctype.h>
    #include <stdbool.h>
    #include <stdlib.h>
    #include <time.h>
    
    int main(){
    
    //初始化程序
    char another_game = 'N';
    bool correct = true;
    int counter = 0;
    int sequence_length = 0;
    time_t seed = 0;
    time_t now = 0;
    int number = 0;
    int time_taken = 0;
    int c;
    
    do{
    	//初始化游戏循环
    	printf("Simon游戏开始...\n");
    	counter = 0;
    	sequence_length = 2;
    	time_taken = clock();
    	correct = true;
    
    	while(correct){
    		sequence_length += (counter++%3 == 0);
    		
    		//生成随机数
    		seed = time(NULL);
    		now = clock();
    		srand((unsigned int)seed);
    
    		for(int i = 1; i <= sequence_length; i++){
    			printf("%d ",rand()%10);
    		}
    
    		//等待1秒
    		for(;clock() - now < CLOCKS_PER_SEC;)
    
    		//删除数字序列
    		printf("\r");
    		for(int i = 1; i <= sequence_length; i++){
    			printf("  ");
    
    		if(counter == 1){
    			printf("\n输入你的序列,别忘记用空格间隔.\n");
    		}else{
    			printf("\r");
    		}
    
    		//读取用户输入
    		//判断:输入是否正确
    		srand((unsigned int)seed);
    		for(int i = 1; i<= sequence_length; i++){
    			scanf("%d",&number);
    			if(number != rand()%10){
    				correct = false;
    				break;
    			}
    		}
    		printf("%s\n",correct?"Correct~":"Wrong!");
    	}
    
    	//结算分数
    	time_taken = (clock() - time_taken)/CLOCKS_PER_SEC;
    	printf("您的得分为:%d",--counter*counter*100/time_taken);
    
    	/*
    	fflush(stdin);
    	linux gcc不支持该扩展.
    	*/
    	//替代方案
    	if (feof(stdin) || ferror(stdin))  
    		{
    			break;
    		}
    	while((c = getchar()) != '\n' && c != EOF);/*可直接将这句代码当成fflush(stdio)的替代，直接运行可清除输入缓存流 */
    
    	//是否开始新的游戏?
    	printf("\n是否开始新的游戏?(y/n)");
    	scanf("%c",&another_game);
    
    }while(toupper(another_game) == 'Y');
    //结束
    return 0;
