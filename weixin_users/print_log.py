# -*- coding:utf-8 -*-


class PrintLog:

    @staticmethod
    def print_start_flag(string):
        PrintLog.print_log(string + "() start......")

    @staticmethod
    def print_end_flag(string):
        PrintLog.print_log(string + "() end.\n")

    @staticmethod
    def print_log(string):
        print("=====================" + string)
