from selectolax.parser import HTMLParser, Node


def get_page_title(page_content: str | bytes) -> str | None:
    parser = HTMLParser(page_content)
    title_tag = parser.css_first('title')
    if title_tag is None:
        return None
    return title_tag.text()