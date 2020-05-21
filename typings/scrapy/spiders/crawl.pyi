"""
This type stub file was generated by pyright.
"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Spider
from typing import Any, Optional

"""
This modules implements the CrawlSpider which is the recommended spider to use
for scraping typical web sites that requires crawling pages.

See documentation in docs/topics/spiders.rst
"""
def _identity(request, response):
    ...

def _get_method(method, spider):
    ...

_default_link_extractor = LinkExtractor()
class Rule(object):
    def __init__(self, link_extractor: Optional[Any] = ..., callback: Optional[Any] = ..., cb_kwargs: Optional[Any] = ..., follow: Optional[Any] = ..., process_links: Optional[Any] = ..., process_request: Optional[Any] = ...):
        self.link_extractor = ...
        self.callback = ...
        self.cb_kwargs = ...
        self.process_links = ...
        self.process_request = ...
        self.process_request_argcount = ...
        self.follow = ...
    
    def _compile(self, spider):
        self.callback = ...
        self.process_links = ...
        self.process_request = ...
        self.process_request_argcount = ...
    
    def _process_request(self, request, response):
        """
        Wrapper around the request processing function to maintain backward
        compatibility with functions that do not take a Response object
        """
        ...
    


class CrawlSpider(Spider):
    rules = ...
    def __init__(self, *a, **kw):
        ...
    
    def parse(self, response):
        ...
    
    def parse_start_url(self, response):
        ...
    
    def process_results(self, response, results):
        ...
    
    def _build_request(self, rule, link):
        ...
    
    def _requests_to_follow(self, response):
        ...
    
    def _response_downloaded(self, response):
        ...
    
    def _parse_response(self, response, callback, cb_kwargs, follow: bool = ...):
        ...
    
    def _compile_rules(self):
        ...
    
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        ...
    

