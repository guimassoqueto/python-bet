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
        # TODO: remover linha abaixo
        popup_close_selector = 'button.sb-modal__close__btn.uk-modal-close-default.uk-icon.uk-close'
        await page.wait_for_selector(selector=popup_close_selector, state='visible')
        await page.click(popup_close_selector)
        # Scroll to the bottom of the page
        # await page.evaluate("window.scrollTo({ top: document.body.scrollHeight / 5, behavior: 'smooth' })")
        await page.wait_for_load_state('networkidle')
        html_content = await page.content()
        await browser.close()
        return html_content
