from playwright.async_api import async_playwright


async def async_get_html_content(url):
    """
    Retrieves the HTML content of a given URL using Playwright.

    Args:
        url (str): The URL to retrieve the HTML content from.

    Returns:
        str: The HTML content of the given URL.
    """
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto(url)
        await page.wait_for_selector(selector='button.sb-modal__close__btn.uk-modal-close-default.uk-icon.uk-close', state='visible', timeout=20000)
        html_content = await page.content()
        await browser.close()
        return html_content
