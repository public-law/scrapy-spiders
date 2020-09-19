from scrapy import Spider
from scrapy.http import Request, Response
from typing import Any, Dict


class DojGlossaries(Spider):
    name = "canada_doj_glossaries"
    start_urls = [
        "https://canada.justice.gc.ca/eng/rp-pr/cp-pm/eval/rep-rap/2019/elf-esc/p7.html",
        "https://www.justice.gc.ca/eng/rp-pr/cp-pm/eval/rep-rap/12/lap-paj/p7g.html",
    ]

    def parse(self, response: Response, **kwargs: Dict[str, Any]):
        """Framework callback which begins the parsing."""
        yield {"url": response.url}