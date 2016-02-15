# -*- coding:utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from weixin_users.items import WeixinUsersItem
from weixin_users.print_log import PrintLog
from weixin_users.weixin_configuration import WeixinCfg

import re
import json


# 使用cookie登录的方法：因为带cookie登录的话，server会认为你是一个已登录的用户，所以就会返回给你一个已登录的内容
# 1)用chrome登录“微信公众平台”, 打开Chrome的"更多工具->开发者工具".
# 2)点击微信管理后台页面的“用户管理”, 取“Request Headers”中的Cookie作为变量cookie_string的值.
# 3)取url作为要抓取的url.
# 4)取url中的token作为变量page_token的值.

class ContactSpider(CrawlSpider):
    PrintLog.print_log(__name__)

    name = "contact"
    allowed_domains = ["weixin.qq.com"]
    total_page_count = 1    # 记录总共多少页
    page_num = 0    # 从第0页开始抓取

    cookie_dict = {}
    contact_manage_page_prefix = 'https://mp.weixin.qq.com/cgi-bin/contactmanage?t=user/index&type=0&lang=zh_CN'
    contact_manage_page_pagesize = '&pagesize='
    contact_manage_page_idx = '&pageidx='
    contact_manage_page_token = '&token='

    def start_requests(self):
        PrintLog.print_start_flag(self.start_requests.__name__)
        self.cookie_dict = self.convert_cookie_string_to_dict(WeixinCfg.cookie_string)
        return [self.request_page(page_idx=self.page_num)]

    def request_page(self, page_idx=0):
        # 组合url
        page_url = self.contact_manage_page_prefix + \
                   self.contact_manage_page_pagesize + WeixinCfg.page_size + \
                   self.contact_manage_page_idx + str(page_idx) + \
                   self.contact_manage_page_token + WeixinCfg.page_token
        # print page_url
        return Request(url=page_url, cookies=self.cookie_dict, callback=self.parse)

    def parse(self, response):
        PrintLog.print_start_flag(self.parse.__name__)
        sel = Selector(response)

        # 取出friendsList
        friends = sel.re(r'friendsList :\s*(.*)')
        yield self.parse_friends_list(friends_list=friends)

        # 取下一页数据
        PrintLog.print_log("get next page")
        page_count_str_list = sel.re(r'pageCount :\s*(.*)')
        m = re.findall(r"\d", page_count_str_list[0])
        self.total_page_count = int(m[0])
        # print "page_count_num=", self.total_page_count
        self.page_num += 1 # 下一页码
        if self.page_num < self.total_page_count:
            yield self.request_page(page_idx=self.page_num)

    # 取出friends_list.contacts的值作为item,交由pipelines处理
    def parse_friends_list(self, friends_list=""):
        PrintLog.print_start_flag(self.parse_friends_list.__name__)
        # print friends_list
        # print type(friends_list)
        # print type(friends_list[0])

        # change to <type 'str'> from <type 'unicode'>
        utf8str = friends_list[0].encode("utf-8")
        '''
        utf8str is:
        ({"contacts":[{"id":"xxxxxx","nick_name":"yingchao1","remark_name":"","group_id":0,"wx_headimg_url":""},
                      {"id":"xxxxxx","nick_name":"yingchao2","remark_name":"","group_id":0,"wx_headimg_url":""}
                     ]}).contacts,
       '''
        first = utf8str.index("[")
        last = utf8str.index("]")
        # self.get_user_name(friends_str=utf8str[(first+1):last])
        item = WeixinUsersItem()
        # 去[]内的字符串作为item
        item['friends_list'] = utf8str[(first+1):last]
        return item

    def convert_cookie_string_to_dict(self, str_of_cookie=""):
        PrintLog.print_start_flag(self.convert_cookie_string_to_dict.__name__)
        str0 = re.sub(r'\s', "", str_of_cookie)
        datadict = {}
        for str1 in str0.split(';'):
            # print str1
            key, value = str1.split('=', 1)
            datadict[key] = value
        # print datadict
        return datadict

    def get_user_name(self, friends_str=""):
        friends_sum= friends_str.split('},')
        for s in friends_sum:
            # 先remove所有[]符号
            s0 = re.sub(r'[{}]', "", s)
            # 在开始和末尾加上[], 成为json格式
            s0 = "{"+s0+"}"
            b = json.loads(s0)
            print b["nick_name"]
            print b["remark_name"]