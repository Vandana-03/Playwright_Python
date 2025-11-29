from playwright.sync_api import Page


def test_maxbrowser(page:Page):
    page.goto("https://google.com")
    page.wait_for_timeout(2000)
    page.viewport_size = {"width": 1920, "height": 1080}
    page.wait_for_timeout(2000)