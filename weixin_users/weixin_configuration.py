# -*- coding:utf-8 -*-


# 使用cookie登录的方法：因为带cookie登录的话，server会认为你是一个已登录的用户，所以就会返回给你一个已登录的内容
# 1)用chrome登录“微信公众平台”, 打开Chrome的"更多工具->开发者工具".
# 2)点击微信管理后台页面的“用户管理”, 取“Request Headers”中的Cookie作为变量cookie_string的值.
# 3)取url作为要抓取的url.
# 4)取url中的token作为变量page_token的值.
class WeixinCfg:

    # ------------- START ------------- #
    # 注意: 要修改下面两个变量的值
    page_token = '474211568'    # 4)取url中的token作为变量page_token的值
    # 2)点击微信管理后台页面的“用户管理”, 取“Request Headers”中的Cookie作为变量cookie_string的值.
    cookie_string = "noticeLoginFlag=1; " \
                    "pgv_pvi=9969913856; " \
                    "data_bizuin=3090797880; " \
                    "data_ticket=AgYZI8wuS2eTNZ2dtBOcBZZSAwHtlnEyjkHBtvmzxYQ=; " \
                    "noticeLoginFlag=1; " \
                    "slave_user=gh_808d3c6c3914; " \
                    "slave_sid=TFdHY2hlR09pNlBYZ05Tb0MzVlZxYkwzcHdISks5SDF5aE9EbGhXU0ZQdDJGN1pnSEtpUGlBV0pFcGxGeDMxMFlyS3JJb1NFUWJ0M3JGaTVjUkE3Tmxva2xBU1RZRGs1RjgzSHo0VkNVS3dkVWx2V0JOUS94Ykw4QWtXRVRORG8=; " \
                    "bizuin=3013511534"
    # ------------- END ------------- #

    page_size = '20'    # 可以修改这个改变每页显示多少个用户

    saved_file = './contacts.xls'    # 数据保存的文件
