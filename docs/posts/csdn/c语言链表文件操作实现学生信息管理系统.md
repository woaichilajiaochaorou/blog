---
title: "c语言链表文件操作实现学生信息管理系统"
date: 2020-03-22
description: "#include<stdio.h>#include<stdlib.h>#include<string.h>#include<time.h>#include <unistd.h>#include<windows.h>struct student{int age;float math;struct student..."
tags:
  - CSDN迁移
---

# c语言链表文件操作实现学生信息管理系统

#include<stdio.h>
    #include<stdlib.h>
    #include<string.h>
    #include<time.h>
    #include <unistd.h>
    #include<windows.h>
    struct student{
       
       
    	int age;
    	float math;
    	struct student *pnext;
    	char stu_name[20];
    	int code;//学生学号 
    };
    
    void menu(){
       
       //操作界面 
     	printf("    |________________________________________________|\n");  
        printf("    |                                                |\n");  
        printf("    |                学生信息管理系统                |\n");  
        printf("    |                                                |\n");  
        printf("    |               [0]退出系统                      |\n");  
        printf("    |               [1]增加学生信息                  |\n");  
        printf("    |               [2]删除学生信息                  |\n");  
        printf("    |               [3]修改学生信息                  |\n");  
        printf("    |               [4]查找学生的信息                |\n");  
        printf("    |               [5]按照学生成绩排序              |\n");  
        printf("    |               [6]浏览全部学生信息              |\n");  
        printf("    |               [7]保存学生信息到文件            |\n");  
        printf("    |               [8]按照学生学号排排序            |\n");  
        printf("    |               [9]打印链表信息                  |\n"); 
    	printf("    |________________________________________________|\n"); 
    }
    void welcome(){
       
       
    	system("color a0"); 
    	printf("***********************************************\n");
    	printf("\n");
    	printf("\n");
    	printf("\n");
    	printf("*************欢迎进入学生信息管理系统**********");
    	printf("\n");
    	printf("\n");
    	printf("\n");
    	printf("************************************************\n");
    } 
    
    void free_link_list(struct student *phead){
       
       
    	struct student *pre=phead;
    	struct student *p=phead->pnext;
    	while(p!=NULL){
       
       
    		free(pre);
    		pre=p;
    		p=p->pnext;
    	}
    }
    
    void save_student(student *phead)
    {
       
       //保存学生信息到文件  
    	FILE *fp=NULL;
    	if(!(fp=fopen("student.txt","w"))){
       
       
    		printf("打开文件失败 \n");
    		exit(0); 
    	}
    	struct student *p=phead->pnext;
    	while(p)
    	{
       
       	
    		fprintf(fp,"%d %s %d %f\n",p->code,p->stu_name,p->age,p->math);//写入文件 
    		p=p->pnext;
    	}
    	fclose(fp);
    	free_link_list(phead);
    }
    void add_student(student *phead)
    {
       
       	
    	system("cls");
    	menu(); 
    	student *pnew=(student*)malloc(sizeof(student));
    	pnew->pnext=phead->pnext;
    	phead
