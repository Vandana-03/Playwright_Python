import time

from playwright.sync_api import Playwright, expect, sync_playwright


def checkbox(playwright: Playwright):
    browser=playwright.chromium.launch(headless=False,slow_mo=900)
    context=browser.new_context()
    page=context.new_page()

    page.goto("https://testing.qaautomationlabs.com/checkbox.php")

    #verify title
    page.wait_for_selector("//div[h1='Checkbox Demo']")
    expect(page.locator("//div[h1='Checkbox Demo']")).to_have_text("Checkbox Demo")

    page.get_by_label("Check me!").check()
    page.wait_for_selector("//div[@id='message']")
    expect(page.locator("//div[@id='message']")).to_have_text("checked")

    page.get_by_label(" Disable Checkbox 3").is_disabled()
    page.locator("#chk4").is_disabled()

    page.get_by_text("Item 1:- Inbox").drag_to(page.locator("Item 5:- Archive"))
    time.sleep(200)
    
    context.close()
    browser.close()

with sync_playwright() as playwright:
    checkbox(playwright)



