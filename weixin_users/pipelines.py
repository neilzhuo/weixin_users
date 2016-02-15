# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import json
import xlwt
from weixin_users.print_log import PrintLog
from weixin_users.weixin_configuration import WeixinCfg


class WeixinUsersPipeline(object):

    PrintLog.print_log(__name__)

    def __init__(self):
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('sheet1', cell_overwrite_ok=True)
        self.row = 0
        self.column = 0
        self.sheet.write(self.row, self.column, "nick_name")
        self.sheet.write(self.row, self.column+1, "remark_name")
        self.row += 1

    def close_spider(self, spider):
        self.book.save(WeixinCfg.saved_file)

    def process_item(self, item, spider):
        PrintLog.print_start_flag(self.process_item.__name__)
        '''
        item['friends_list'] is:
        {"id":"xxxxxx","nick_name":"yingchao1","remark_name":"","group_id":0,"wx_headimg_url":""},
        {"id":"xxxxxx","nick_name":"yingchao2","remark_name":"","group_id":0,"wx_headimg_url":""}
        '''
        friends_str = item['friends_list']
        friends_sum= friends_str.split('},')
        for s in friends_sum:
            # 先remove所有{}符号
            s0 = re.sub(r'[{}]', "", s)
            # 在开始和末尾加上{}, 成为json格式
            s0 = "{"+s0+"}"
            b = json.loads(s0)
            # print b["nick_name"], b["remark_name"]
            self.sheet.write(self.row, self.column, b["nick_name"])
            self.sheet.write(self.row, self.column+1, b["remark_name"])
            self.row += 1
        return item
