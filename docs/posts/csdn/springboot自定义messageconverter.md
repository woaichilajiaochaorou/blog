---
title: "springboot自定义messageConverter"
date: 2021-08-24
tags:
  - CSDN迁移
---

# springboot自定义messageConverter

## 如果想自定义传输数据的类型 需要设置自己的messageConverter
    
    
    public class YanMessageConverter implements HttpMessageConverter {
        @Override
        public boolean canRead(Class clazz, MediaType mediaType) {
    
            return false;
        }
    
        @Override
        public boolean canWrite(Class clazz, MediaType mediaType) {
            return clazz.isAssignableFrom(Car.class);
        }
    
        @Override
        public List&lt;MediaType&gt; getSupportedMediaTypes() {
            MediaType mediaType = MediaType.parseMediaType("application/yan");
            ArrayList&lt;MediaType&gt; objects = new ArrayList<>();
            objects.add(mediaType);
            return objects;
        }
    
        @Override
        public Object read(Class clazz, HttpInputMessage inputMessage) throws IOException, HttpMessageNotReadableException {
            return null;
        }
    
        @Override
        public void write(Object o, MediaType contentType, HttpOutputMessage outputMessage) throws IOException, HttpMessageNotWritableException {
            Car o1 = (Car) o;
            String data="hello "+((Car) o).getName()+" hello "+((Car) o).getPrice();
            OutputStream body = outputMessage.getBody();
            String s = new String(data.getBytes(), "UTF-8");
            System.out.println(s);
            body.write(s.getBytes("gbk"));//避免乱码
    
        }
    }
    
    
    
    
    @Import(User.class)
    @Configuration(proxyBeanMethods = true)
    @EnableConfigurationProperties(Car.class)
    //proxyBeanMEthods
    // 设置为false意味着跳过扫描容器的步骤，直接new一个新的组件而不是使用容器中的组件
    public class MyConfiguration implements WebMvcConfigurer {
        @Bean
        @ConditionalOnClass(name = "Pet")
        public User getUser(){
            return new User("yan",18,getPet());
        }
        //@Bean("tom")
        public Pet getPet(){
            return new Pet("tom");
        }
    
        @Override
        public void configurePathMatch(PathMatchConfigurer configurer) {
            UrlPathHelper urlPathHelper = new UrlPathHelper();
            urlPathHelper.setRemoveSemicolonContent(false);
            configurer.setUrlPathHelper(urlPathHelper);
        }
    //自定义转换器，转换自定义的字符串格式
        @Override
        public void addFormatters(FormatterRegistry registry) {
            registry.addConverter(new Converter&lt;String, Pet&gt;() {
                @Override
                public Pet convert(String source) {
                    String[] split = source.split(",");
                    return new Pet(split[0]);
                }
            });
        }
    	//如果想把自定义的类型也融入到参数内容协商里面去
    	//需要重写内容协商配置类
    	//注意：这里会覆盖所有的映射
    	//所以我们需要自己添加映射 
        @Override
        public void configureContentNegotiation(ContentNegotiationConfigurer configurer) {
            //configurer.strategies();
            HashMap&lt;String, MediaType&gt; stringMediaTypeHashMap = new HashMap<>();
            stringMediaTypeHashMap.put("xml",MediaType.APPLICATION_XML);
            stringMediaTypeHashMap.put("json",MediaType.APPLICATION_JSON);
            stringMediaTypeHashMap.put("yan",MediaType.parseMediaType("application/yan"));
            //参数响应
            ParameterContentNegotiationStrategy parameterContentNegotiationStrategy = new ParameterContentNegotiationStrategy(stringMediaTypeHashMap);
    
            //若想基于头的响应 则应该增加策略
            HeaderContentNegotiationStrategy headStrategy=new HeaderContentNegotiationStrategy();
    
    
            configurer.strategies(Arrays.asList(parameterContentNegotiationStrategy,headStrategy));
    
        }
    	//添加自定义messageConverter
        @Override
        public void extendMessageConverters(List&lt;HttpMessageConverter&lt;?&gt;> converters) {
            converters.add(new YanMessageConverter());
        }
    }
