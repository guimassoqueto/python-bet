from fake_useragent import UserAgent


def get_user_agent() -> str:
    """
    Returns a random user agent string.

    :return: A randomly generated user agent string.
    :rtype: str
    """
    ua = UserAgent(browsers=['chrome'], os=['linux']).random
    return ua