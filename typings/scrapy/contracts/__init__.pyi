"""
This type stub file was generated by pyright.
"""

import sys
import re
from functools import wraps
from inspect import getmembers
from unittest import TestCase
from scrapy.http import Request
from scrapy.utils.spider import iterate_spider_output
from scrapy.utils.python import get_spec

class ContractsManager(object):
    contracts = ...
    def __init__(self, contracts):
        ...
    
    def tested_methods_from_spidercls(self, spidercls):
        ...
    
    def extract_contracts(self, method):
        ...
    
    def from_spider(self, spider, results):
        ...
    
    def from_method(self, method, results):
        ...
    
    def _clean_req(self, request, method, results):
        """ stop the request from returning objects and records any errors """
        ...
    


class Contract(object):
    """ Abstract class for contracts """
    request_cls = ...
    def __init__(self, method, *args):
        self.testcase_pre = ...
        self.testcase_post = ...
        self.args = ...
    
    def add_pre_hook(self, request, results):
        ...
    
    def add_post_hook(self, request, results):
        ...
    
    def adjust_request_args(self, args):
        ...
    


def _create_testcase(method, desc):
    class ContractTestCase(TestCase):
        ...
    
    

