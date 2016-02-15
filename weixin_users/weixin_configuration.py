# -*- coding:utf-8 -*-


# 使用cookie登录的方法：因为带cookie登录的话，server会认为你是一个已登录的用户，所以就会返回给你一个已登录的内容
# 1)用chrome登录“微信公众平台”, 打开Chrome的"更多工具->开发者工具".
# 2)点击微信管理后台页面的“用户管理”, 取“Request Headers”中的Cookie作为变量cookie_string的值.
# 3)取url作为要抓取的url.
# 4)取url中的token作为变量page_token的值.
class WeixinCfg:

    # ------------- START ------------- #
    # 注意: 要修改下面两个变量的值
    page_token = '613899957'    # 4)取url中的token作为变量page_token的值
    # 2)点击微信管理后台页面的“用户管理”, 取“Request Headers”中的Cookie作为变量cookie_string的值.
    cookie_string = "noticeLoginFlag=1; " \
                    "remember_acct=zhuoyc2002%40163.com; " \
                    "data_bizuin=3090797880; " \
                    "data_ticket=AgZEL1JIZ8c10EzAdtEv+wB8AwHegJqEBvPo5S77pAQ=; " \
                    "noticeLoginFlag=1; " \
                    "remember_acct=18929583193%40163.com; " \
                    "slave_user=gh_808d3c6c3914; " \
                    "slave_sid=bGFyZlpqRGZGS1JrTEpWMTQ1VVdXZnZBR1pJNFhGUnVKYWNmRXV4bUM1N3dqcUlMRXU3Ump5Z0QwZUN" \
                    "zM1lsTmk2OXg3YTBiZm05eG1BeWpjMWZDZ2NZNWx2NmY5WVNyRjNMMGlWcEdDTFZGY2lBVGVhbUd0UlBxdXNZbDR2VkI=; " \
                    "bizuin=3013511534"
    # ------------- END ------------- #

    page_size = '20'    # 可以修改这个改变每页显示多少个用户

    saved_file = './contacts.xls'    # 数据保存的文件
