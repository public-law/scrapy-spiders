"""
This type stub file was generated by pyright.
"""

import logging
from twisted.internet import defer
from scrapy import signals

"""This module implements the Scraper component which parses responses and
extracts information from them"""
logger = logging.getLogger(__name__)
class Slot(object):
    """Scraper slot (one per running spider)"""
    MIN_RESPONSE_SIZE = ...
    def __init__(self, max_active_size=...):
        self.max_active_size = ...
        self.queue = ...
        self.active = ...
        self.active_size = ...
        self.itemproc_size = ...
        self.closing = ...
    
    def add_response_request(self, response, request):
        ...
    
    def next_response_request_deferred(self):
        ...
    
    def finish_response(self, response, request):
        ...
    
    def is_idle(self):
        ...
    
    def needs_backout(self):
        ...
    


class Scraper(object):
    def __init__(self, crawler):
        self.slot = ...
        self.spidermw = ...
        self.itemproc = ...
        self.concurrent_items = ...
        self.crawler = ...
        self.signals = ...
        self.logformatter = ...
    
    @defer.inlineCallbacks
    def open_spider(self, spider):
        """Open the given spider for scraping and allocate resources for it"""
        self.slot = ...
    
    def close_spider(self, spider):
        """Close a spider being scraped and release its resources"""
        ...
    
    def is_idle(self):
        """Return True if there isn't any more spiders to process"""
        ...
    
    def _check_if_closing(self, spider, slot):
        ...
    
    def enqueue_scrape(self, response, request, spider):
        ...
    
    def _scrape_next(self, spider, slot):
        ...
    
    def _scrape(self, response, request, spider):
        """Handle the downloaded response or failure through the spider
        callback/errback"""
        ...
    
    def _scrape2(self, request_result, request, spider):
        """Handle the different cases of request's result been a Response or a
        Failure"""
        ...
    
    def call_spider(self, result, request, spider):
        ...
    
    def handle_spider_error(self, _failure, request, response, spider):
        ...
    
    def handle_spider_output(self, result, request, response, spider):
        ...
    
    def _process_spidermw_output(self, output, request, response, spider):
        """Process each Request/Item (given in the output parameter) returned
        from the given spider
        """
        ...
    
    def _log_download_errors(self, spider_failure, download_failure, request, spider):
        """Log and silence errors that come from the engine (typically download
        errors that got propagated thru here)
        """
        ...
    
    def _itemproc_finished(self, output, item, response, spider):
        """ItemProcessor finished for the given ``item`` and returned ``output``
        """
        ...
    


