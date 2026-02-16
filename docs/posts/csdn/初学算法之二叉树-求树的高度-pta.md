---
title: "初学算法之二叉树---求树的高度 pta"
date: 2021-07-15
description: "#include <stdio.h>#include <stdlib.h>#include <algorithm>typedef char ElementType;typedef struct TNode *Position;typedef Position BinTree;struct TNode{    ElementType Data;    BinTree Left;    BinTree"
tags:
  - CSDN迁移
---

# 初学算法之二叉树---求树的高度 pta

#include <stdio.h>
    #include <stdlib.h>
    #include <algorithm>
    typedef char ElementType;
    typedef struct TNode *Position;
    typedef Position BinTree;
    struct TNode{
        ElementType Data;
        BinTree Left;
        BinTree Right;
    };
    
    BinTree CreatBinTree(); /* 实现细节忽略 */
    int GetHeight( BinTree BT );
    
    int main()
    {
        BinTree BT = CreatBinTree();
        printf("%d\n", GetHeight(BT));
        return 0;
    }
    /* 你的代码将被嵌在这里 */
    
    int GetHeight( BinTree BT ){
    	int high=0;
    	if(BT==NULL){
    		return 0;
    	}
    	high++;
    	int lh=GetHeight(BT->Left);
    	int rh=GetHeight(BT->Right);
    	int max=0;
    	if(lh>rh){//左右比较选择最高的树
            max=lh;
        }else{
            max=rh;
        }
    	return high+max;
    }
