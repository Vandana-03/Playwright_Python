import time

from playwright.sync_api import Playwright, Page, sync_playwright

def test_automate(playwright:Playwright):
    browser =playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testing.qaautomationlabs.com/index.php")

    page.locator("//h1[normalize-space()='Tools Demo']").get_by_title("Tools Demo")
    page.get_by_role("link", name="CheckBox", exact=True).click()
    page.get_by_title("Checkbox Demo", name="Checkbox Demo", exact=True)

    time.sleep(44)

with sync_playwright() as playwright:
    test_automate(playwright)