import re
from typing import Any, Dict, List

SEPARATOR = re.compile(r"[,&]")


def statute_meta(text: str) -> List[str]:
    """Parse a statute meta line of text.

    For example:
      input:  'ORS 181A.235 & ORS 192'
      output: ['ORS 181A.235', 'ORS 192']
    """
    return [s.strip() for s in SEPARATOR.split(text)]


def meta_sections(text: str) -> Dict[str, Any]:
    authority, implements, history = text.split("<br>", maxsplit=2)

    return {
        "authority": statute_meta(authority.split("</b>")[1].strip()),
        "implements": [implements.split("</b>")[1].strip()],
        "history": history.replace("<b>History:</b><br>", "").replace("<br></p>", ""),
    }
