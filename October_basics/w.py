import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testing.qaautomationlabs.com/notifications.php")
    page.get_by_role("heading", name="Notification Demo").click()


    page.get_by_role("button", name="Success Message").click()
    page.get_by_text("Notification Body:- You").click()

    page.get_by_role("button", name="Info Message").click()
    page.get_by_text("Notification Body:- You").first.click()

    page.get_by_role("button", name="Primary Message").click()
    page.get_by_text("Notification Body:- You").first.click()

    page.get_by_role("button", name="Error Message").click()
    page.get_by_text("Notification Body:- You").first.click()

    page.get_by_role("button", name="Close").first.click()
    page.get_by_role("button", name="Close").first.click()
    page.get_by_role("button", name="Close").first.click()
    page.get_by_role("button", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
