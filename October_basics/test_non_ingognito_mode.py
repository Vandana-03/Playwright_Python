from playwright.sync_api import Page

def test_launch(page: Page):
    page.goto("https://google.com")

#Open browser in Non Incognito mode


