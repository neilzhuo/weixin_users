# Scrapy all user infos of weixin gongzong hao by using scrapy

抓取指定微信公众号的所有关注用户. 使用Scrapy框架.
使用cookie登录的方法: 因为带cookie登录的话,server会认为你是一个已登录的用户,所以就会返回给你一个已登录的内容.

做这个事情主要是源于一个朋友咨询是否可以导出公众号中的关注用户，和自己的好友进行相关性对比。然后发现微信没有提供任何方法导出关注用户和好友列表，所以：
- 1. 写了这个用来导出微信公众号的关注用户到excel。
- 2. 另外再想到一个方法导出微信好友：微信提供了一个群发功能（"设置"->"通用"->"功能"->"群发助手"），使用这个功能，“新建群发”->"全选"->"下一步",这样就会生成包含全部好友名的图片，抓屏生成图片，把这个图片转到电脑上，用office的ocr功能识别这个图片里面的文字，好了，好友列表也就有了。（当然也有软件提供导出微信好友这个功能，但是装这些不明来历的软件总是心里不放心啊。）

# 运行环境
- Ubuntu 14.04.3 LTS
- Python 2.7.6
- Scrapy 1.0.5

# 修改文件weixin_configuration.py中定义的变量值
修改weixin_configuration.py中变量的值:
- 1)用chrome登录“微信公众平台”,打开Chrome的"更多工具->开发者工具".
- 2)cookie_string: 点击微信管理后台页面的“用户管理”,取“Request Headers”中的Cookie作为变量cookie_string的值.
- 3)page_token: 取url中的token作为变量page_token的值.
- 4)page_size: 自己填一个值即可.
- 5)saved_file: 保存的文件名.
- 6)取url作为要抓取的url. 如果微信改了url, 需要修改文件contact_spider.py中的变量contact_manage_page_prefix.

# run
```
$ cd ./weixin_users
$ ls
README.md  scrapy.cfg  weixin_users
$ scrapy crawl contact
```
