---
title: "java url调用接口"
date: 2021-05-25
description: "话不多说 上步骤url = new URL('你的url');//设置请求方式HttpURLConnection connection = (HttpURLConnection) url.openConnection();connection.setRequestMethod('GET');connection.setRequestProperty('content-type', 'applica"
tags:
  - CSDN迁移
---

# java url调用接口

话不多说 上步骤
    
    
    url = new URL("你的url");
    //设置请求方式
    HttpURLConnection connection = (HttpURLConnection) url.openConnection();
    connection.setRequestMethod("GET");
    connection.setRequestProperty("content-type", "application/json;charset=utf-8");
     //连接
     connection.connect();
      //输出
            String line;
            InputStream is = null;
            if (connection.getResponseCode() == status) {
                //解码gzip格式的json
                is = new GZIPInputStream(connection.getInputStream());
    
                BufferedReader reader = new BufferedReader(new InputStreamReader(is));
                StringBuilder sb=new StringBuilder();
                while ((line = reader.readLine()) != null) {
                    sb.append(line);
                }
                weatherString=sb.toString();
