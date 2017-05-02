# coding: utf-8
import json

import os
import requests
from . import helpers
from .webtrader import WebTrader


class GFTrader2(WebTrader):
    config_path = os.path.dirname(__file__) + '/config/gf2.json'

    def __init__(self, debug=True):
        super(GFTrader2, self).__init__(debug=debug)
        self.cookie = None
        self.account_config = None
        self.s = None
        self.client = requests.session()
        self.exchange_stock_account = dict()
        self.config = helpers.file2dict(self.config_path)

    def _request(self, method, params=None):
        content = self.client.request('GET', self.config['server'] + '/' + method, params)
        if content.status_code == 200:
            print('error http code:%s' % content.status_code)
        # @todo 异常处理
        return json.loads(content.text)

    def login(self, throw=False):
        print('login')
        return

    def buy(self, stock_code, price, amount=0, volume=0, entrust_prop=0):
        # :param stock_code: 股票代码
        # :param price: 买入价格
        # :param amount: 买入股数
        # :param volume: 买入总金额 由 volume / price 取 100 的整数， 若指定 amount 则此参数无效
        # :param entrust_prop: 委托类型，暂未实现，默认为限价委托
        return self._request('buy', {
            'code': stock_code,
            'price': price,
            'amount': amount
        })

    def sell(self, stock_code, price, amount=0, volume=0, entrust_prop=0):
        """卖出
        :param stock_code: 股票代码
        :param price: 卖出价格
        :param amount: 卖出股数
        :param volume: 卖出总金额 由 volume / price 取整， 若指定 amount 则此参数无效
        :param entrust_prop: 委托类型，暂未实现，默认为限价委托
        """
        return self._request('sell', {
            'code': stock_code,
            'price': price,
            'amount': amount
        })

    def get_balance(self):
        """获取账户资金状况"""
        return self._request('balance')

    def cancel_entrust(self, entrust_no):
        # 撤单
        # :param entrust_no: 委单号
        return self._request('sell', {
            'id': entrust_no
        })

    def get_position(self):
        """获取持仓"""
        return self._request('position')

    def get_entrust(self, action_in=1):
        '''
        只支持查询可撤委托
        :param action_in: 当值为0，返回全部委托；当值为1时，返回可撤委托
        :return:
        '''
        return self._request('pending')
