---
title: "webSocket获取httpsession"
date: 2021-05-21
description: "websocket使用握手拦截器public class HttpSessionHandshakeInterceptor extends org.springframework.web.socket.server.support.HttpSessionHandshakeInterceptor {    @Override    public boolean beforeHandshake(Serv"
tags:
  - CSDN迁移
---

# webSocket获取httpsession

websocket使用握手拦截器
    
    
    public class HttpSessionHandshakeInterceptor extends org.springframework.web.socket.server.support.HttpSessionHandshakeInterceptor {
        @Override
        public boolean beforeHandshake(ServerHttpRequest request, ServerHttpResponse response, WebSocketHandler wsHandler, Map<String, Object> attributes) throws Exception {
            if (request instanceof HttpRequest){
              ServletServerHttpRequest httpRequest=(ServletServerHttpRequest) request;
                HttpSession session = httpRequest.getServletRequest().getSession();
                if (session!=null){
                    //放入attributes中在wshandler中调用websocketsession.getAttributes.get("cueenetSession")即可获得session
                    attributes.put("currentSession",session);
                }
            }
    
            return super.beforeHandshake(request,response,wsHandler,attributes);
        }
    }
    

这是websocket的配置类
    
    
    @Configuration
    @EnableWebSocket
    @EnableWebMvc
    public class WebSocketConfig  implements WebSocketConfigurer {
        @Override
        public void registerWebSocketHandlers(WebSocketHandlerRegistry Registry) {
    //在后面加入了握手拦截器        
            Registry.addHandler(myHandler(),"/websocket").addInterceptors(HandShakeInterceptor());
        }
        @Bean
        public WebsocketHandler myHandler(){
            return new WebsocketHandler();
        }
        @Bean
        public HttpSessionHandshakeInterceptor HandShakeInterceptor(){
            return new HttpSessionHandshakeInterceptor();
        }
    }
    

**以下是websockethandler**
    
    
    public class WebsocketHandler implements WebSocketHandler {
        /**
         * 连接人数
         */
        private static int onlineCounts=0;
    
        private static Map<String, WebSocketSession> clients = new ConcurrentHashMap<String, WebSocketSession>(20);
        /**
         * 连接时客户端session
         */
        private Session  session;
        /**
         * 用户名称，用于区分不同的用户session
         */
        private String username;
    
        @Override
        public void afterConnectionEstablished(WebSocketSession session) throws Exception {
            System.out.println("开始连接...");
            //刚好有个session.getAttributes的方法是不是很巧
            HttpSession httpSession = (HttpSession) session.getAttributes().get("currentSession");
            User user = (User) httpSession.getAttribute("user");
            System.out.println(user.getUsername());
        }
    
        @Override
        public void handleMessage(WebSocketSession session, WebSocketMessage<?> message) throws Exception {
            session.sendMessage(new TextMessage("hello client"));
            System.out.println("收到消息了");
        }
    
        @Override
        public void handleTransportError(WebSocketSession session, Throwable exception) throws Exception {
          exception.printStackTrace();
        }
    
        @Override
        public void afterConnectionClosed(WebSocketSession session, CloseStatus status) throws Exception {
          session.close();
        }
    
        @Override
        public boolean supportsPartialMessages() {
           return false;
        }
    
    
        public void setUsername(String username) {
            this.username = username;
        }
    
    
    
    }
