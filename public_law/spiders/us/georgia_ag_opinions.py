from scrapy import Spider
from scrapy.http import Request, Response


class GeorgiaAgOpinions(Spider):
    """Scrape the Georgia Attorney General Opinions

    Retrieve both the official and unofficial opinions,
    producing one JSON object per opinion (page).
    """

    name = "georgia_ag_opinions"
    start_urls = [
        "https://law.georgia.gov/opinions/official",
        "https://law.georgia.gov/opinions/unofficial",
    ]

    def parse(self, response: Response):
        """Framework callback which begins the parsing."""
        return self.parse_index_page(response)

    def parse_index_page(self, response: Response):
        #
        # Find all the individual opinions on this index page
        # and parse them.
        #

        opinion_paths = response.xpath(
            "//td[contains(@class, 'views-field-title')]/a/@href"
        ).getall()

        for url in [response.urljoin(p) for p in opinion_paths]:
            yield Request(url, callback=self.parse_opinion_page)

        #
        # Go to the next index page, if there is one.
        #

        next_page_path = response.xpath(
            "//a[contains(@title, 'Go to next page')]/@href"
        ).get()

        if next_page_path is not None:
            yield Request(
                response.urljoin(next_page_path), callback=self.parse_index_page
            )

    def parse_opinion_page(self, response: Response):
        yield {"Opinion URL": response.url}