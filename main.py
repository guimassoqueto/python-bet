from app.packages.browser.selenium import sync_get_html_content as se_get_content

if __name__ == "__main__":


    html_content = se_get_content(sporting_bet)
    print(html_content)