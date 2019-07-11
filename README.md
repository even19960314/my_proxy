# 爬虫代理迷你框架

#### 介绍
{

在使用requests模块做爬虫时，经常使用到代理做爬虫，我们这个爬虫框架配置一个代理模块就可以实现每次请求自动使用用代理}

#### 软件架构
有两个文件

​	1、spider.py

​			主程序

​	2、proxy_api.py

​			自己的代理接口程序


#### 安装教程

1. 将两个文件放在要使用的文件下

#### 使用说明

1. 重构proxy_api.py里的get_proxies函数

   1. get_proxies返回一个代理ip
   2. 返回值格式：{'port': '43437', 'ip': '115.211.230.124'}

2. spider.py说明

   

   1. 实例化spider = Spider( proxy = False)

      1. 参数：proxy = false ,不启用代理
      2. 参数：proxy = false ,启用代理

   2. 方法

      1. spider.get_html(url)
         1. 使用get请求获取url源代码
         2. 如果实例化Spider时proxy设置为True，那么get_html(url)自动使用代理去请求
         3. 如果连续拉取代理3次，代理不能用则报错
      2. def get_info(self, url, **regexs):
         1. 参数
            1. url:目标网址
            2. **regexs:  可传多个要在网页中提取数据的正则
         2. return
            1. 返回正则匹配到的数据

   3. 示例：

      不使用代理

      ```
      url = 'http://httpbin.org/ip'
      
      x = Spider()
      
      info = x.get_html(url)
      
      print(info)
      
      #'{\n  "origin": "120.244.63.255, 120.244.63.255"\n}\n'
      ```
      使用代理        

          url = 'http://httpbin.org/ip'
          
          x = Spider(True)
          
          info = x.get_html(url)
          
          print(info)
          
          #'{\n  "origin": "60.168.11.128, 60.168.11.128"\n}\n'
      get_info 方法使用      

          url = 'https://www.x23us.com/class/1_101.html'
          
          book_name_url_regex = '\[简介\]</a><a href="(.*?)" target="_blank">(.*?)</a></td>'
          
          author_regex = '</a></td>\s+?<td class="C">(.*?)</td>'
          
          x = Spider(True)
          
          info = x.get_info(
              url,
              book_name_url = book_name_url_regex,
              author = author_regex,
              )
          
          print(info)
          
          ########################
          {
          	'book_name_url': [
          ('http://www.x23us.com/html/60/60860/', '武极天尊'), 		    ('http://www.x23us.com/html/60/60781/', '武破虚空') ... ...],
          	'author': [
          	'萧晓笑', '平凡心'... ...]
          }

   

#### 参与贡献

1. Fork 本仓库
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request


#### 码云特技

1. 使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2. 码云官方博客 [blog.gitee.com](https://blog.gitee.com)
3. 你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解码云上的优秀开源项目
4. [GVP](https://gitee.com/gvp) 全称是码云最有价值开源项目，是码云综合评定出的优秀开源项目
5. 码云官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6. 码云封面人物是一档用来展示码云会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)