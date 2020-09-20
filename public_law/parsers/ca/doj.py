from typing import List, NamedTuple, Union
from scrapy import Selector
from scrapy.http import Response
from public_law.text import normalize_whitespace
from typing_extensions import Protocol

from datetime import datetime, date
import pytz


class ParseException(Exception):
    pass


class GlossaryEntry(NamedTuple):
    phrase: str
    definition: str


class GlossarySourceParseResult(NamedTuple):
    """All the info about a glossary source"""

    name: str
    source_url: str
    author: str
    pub_date: str
    scrape_date: str
    entries: List[GlossaryEntry]


def parse_glossary(html: Response) -> GlossarySourceParseResult:
    main = html.css("main")

    name = first(main, "h1::text", "name") + "; " + first(main, "h2::text", "name")
    pub_date = first(html, "dl#wb-dtmd time::text", "Pub. date")

    entries: List[GlossaryEntry] = []
    first_list = html.css("main dl")[0]
    for prop in first_list.xpath("dt"):
        entries.append(
            GlossaryEntry(
                phrase=prop.xpath("normalize-space(strong/text())").get(),
                definition=prop.xpath(
                    "normalize-space(./following-sibling::dd/text())"
                ).get(),
            )
        )

    return GlossarySourceParseResult(
        name=name,
        source_url=html.url,
        author="Department of Justice Canada",
        pub_date=pub_date,
        scrape_date=todays_date(),
        entries=entries,
    )


def first(node: Union[Response, Selector], css: str, expected: str) -> str:
    result = node.css(css).get()
    if result is None:
        raise ParseException(f"Could not parse the {expected}")
    return normalize_whitespace(result)


class SimpleTimezone(Protocol):
    def localize(self, dt: datetime) -> date:
        ...


def todays_date() -> str:
    mountain: SimpleTimezone = pytz.timezone("US/Mountain")
    fmt = "%Y-%m-%d"
    return mountain.localize(datetime.now()).strftime(fmt)
