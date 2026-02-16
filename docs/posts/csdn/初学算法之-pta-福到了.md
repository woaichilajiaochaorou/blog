---
title: "初学算法之---pta 福到了"
date: 2021-07-21
description: "import java.io.BufferedReader;import java.io.IOException;import java.io.InputStreamReader;/** * @ClassName 福到了 * @Author ACER * @Description ToDo * @Date 2021/7/19 21:14 * @Version 1.0 **/public class"
tags:
  - CSDN迁移
---

# 初学算法之---pta 福到了

import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    
    
    /**
     * @ClassName 福到了
     * @Author ACER
     * @Description ToDo
     * @Date 2021/7/19 21:14
     * @Version 1.0
     **/
    public class Main
    {
        private static BufferedReader reader=new BufferedReader(new InputStreamReader(System.in));
    
        public static void main(String[] args) throws IOException {
           String []array=new String[101];
    
            String data = reader.readLine();
            String[] s = data.split(" ");
            String character = s[0];
            String rows = s[1];
    
    
    
            for (int i = 0; i < Integer.parseInt(rows); i++) {
                //读入数据
                String lie = reader.readLine();
                array[i]=lie;
            }
    
            //判断数组是否头尾一致
            int j= Integer.parseInt(rows)-1;
            boolean flag=true;
            for (int i = 0; i <=j; i++) {
                if (!array[i].equals(array[j])){
                    flag=false;
                }
                j--;
            }
    
            if(!flag){
                //如果出现头尾不相等情况 需要倒置
                for (int i =  Integer.parseInt(rows)-1; i >=0; i--) {
                    char[] chars = array[i].toCharArray();
    
                    for (int i1 = chars.length-1; i1 >=0 ; i1--) {
                        if ((chars[i1]+"").equals(" ")){
                            System.out.print(" ");
                        }else {
                            System.out.print(character);
                        }
                    }
                    System.out.println();
                }
            }
            else {
                System.out.println("bu yong dao le");
                for (int i = 0; i < Integer.parseInt(rows); i++) {
                    char[] chars = array[i].toCharArray();
                    for (int k = 0; k < array[i].length(); k++) {
                        if ((chars[k]+"").equals(" ")){
                            System.out.print(" ");
                        }else {
                            System.out.print(character);
                        }
                    }
                    System.out.println();
                }
            }
    
        }
    }
