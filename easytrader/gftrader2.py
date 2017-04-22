# coding: utf-8
import json
import os

import requests

from . import helpers
from .webtrader import WebTrader


class GFTrader2(WebTrader):
    config_path = os.path.dirname(__file__) + '/config/gf2.json'

    def __init__(self, debug=True):
        super(GFTrader, self).__init__(debug=debug)
        self.cookie = None
        self.account_config = None
        self.s = None
        self.exchange_stock_account = dict()
        self.sessionid = ''
        self.holdername = list()

    def _prepare_account(self, user, password, **kwargs):
        self.account_config = {
            port: "3000"
        }
        pass

    def login(self, throw=False):
        
        pass

    def create_basic_params(self):
        basic_params = dict(
            dse_sessionId=self.sessionid
        )
        return basic_params

    def request(self, params):
        # todo
        pass

    def format_response_data(self, data):
        pass

    def check_login_status(self, response):
        # todo
        pass

    def check_account_live(self, response):
        # todo
        pass

    def buy(self, stock_code, price, amount=0, volume=0, entrust_prop=0):
        """买入
        :param stock_code: 股票代码
        :param price: 买入价格
        :param amount: 买入股数
        :param volume: 买入总金额 由 volume / price 取 100 的整数， 若指定 amount 则此参数无效
        :param entrust_prop: 委托类型，暂未实现，默认为限价委托
        """
       # todo
       pass

    def sell(self, stock_code, price, amount=0, volume=0, entrust_prop=0):
        """卖出
        :param stock_code: 股票代码
        :param price: 卖出价格
        :param amount: 卖出股数
        :param volume: 卖出总金额 由 volume / price 取整， 若指定 amount 则此参数无效
        :param entrust_prop: 委托类型，暂未实现，默认为限价委托
        """
        # todo
        pass

    def cancel_entrust(self, entrust_no):
        """撤单
        :param entrust_no: 委单号"""
        # todo
       pass

    @property
    def get_position(self):
        # todo
        """获取持仓"""
        pass
    def exchangebill(self):
        pass

    def get_exchangebill(self, start_date, end_date):
        pass

    @property
    def exit(self):
        '''
        退出系统
        :return:
        '''
        # todo
        pass

    def get_entrust(self, action_in=1):
        '''
        只支持查询可撤委托
        :param action_in: 当值为0，返回全部委托；当值为1时，返回可撤委托
        :return:
        '''
        # todo
        pass
