from selenium import webdriver


def sync_get_html_content(url: str) -> str:
    """
    Retrieves the HTML content of a given URL.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the URL.

    """
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(15)
    # TODO: wait for page completely load
    html_content = driver.page_source
    driver.quit()
    return html_content
