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
import pdb


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
        #pdb.set_trace()
        '''
        item['friends_list'] is:
        {id:"xxxxxx",nick_name:"yingchao1",remark_name:"",group_id:[]},
        {id:"xxxxxx",nick_name:"yingchao2",remark_name:"",group_id:[]}
        '''
        friends_str = item['friends_list']
        # 下面的正则表达式要查找和取出字符串‘{...}’
        friends_list= re.findall(r'{[\s\S]*?}', friends_str)
        for s in friends_list:
            # 改为json字符串格式
            s = re.sub(r'\bid\b\b', "\"id\"", s)
            s = re.sub(r'\bnick_name\b', "\"nick_name\"", s)
            s = re.sub(r'\bremark_name\b', "\"remark_name\"", s)
            s = re.sub(r'\bcreate_time\b', "\"create_time\"", s)
            s = re.sub(r'\bgroup_id\b', "\"group_id\"", s)
            b = json.loads(s)
            # print b["nick_name"], b["remark_name"]
            self.sheet.write(self.row, self.column, b["nick_name"])
            self.sheet.write(self.row, self.column+1, b["remark_name"])
            self.row += 1
        return item
