from selenium import webdriver
import asyncio
from selenium import webdriver


async def async_get_html_content(url: str) -> str:
    """
    Retrieves the HTML content of a given URL asynchronously.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the URL.

    """
    driver = webdriver.Chrome()
    await asyncio.sleep(0)  # Allow event loop to switch tasks
    await driver.get(url)
    await asyncio.sleep(15)  # Wait for 15 seconds
    # TODO: wait for page completely load
    html_content = await driver.page_source
    await driver.quit()
    return html_content
