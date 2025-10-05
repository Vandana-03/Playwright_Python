import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page.goto("https://testing.qaautomationlabs.com/checkbox.php")
    page.get_by_role("heading", name="Checkbox Demo").click()
    page.get_by_text("Single Checkbox Demo").click()
    page.get_by_role("checkbox", name="Check me!").check()
    page.get_by_text("checked").click()
    page.get_by_text("Disabled Checkbox Demo").click()
    page.get_by_role("checkbox", name="Enable Checkbox 1").check()
    page.get_by_role("checkbox", name="Enable Checkbox 2").check()
    page.get_by_text("Multiple Checkbox Demo").click()
    page.get_by_role("checkbox", name="Checkbox 1", exact=True).check()
    page.get_by_role("checkbox", name="Checkbox 2", exact=True).check()
    page.get_by_role("checkbox", name="Checkbox 3", exact=True).check()
    page.get_by_role("checkbox", name="Checkbox 4", exact=True).check()
    page.get_by_role("checkbox", name="Checkbox 1", exact=True).uncheck()
    page.get_by_role("checkbox", name="Checkbox 2", exact=True).uncheck()
    page.get_by_role("checkbox", name="Checkbox 3", exact=True).uncheck()
    page.get_by_role("checkbox", name="Checkbox 4", exact=True).uncheck()
    page.get_by_role("button", name="Check All").click()
    page.get_by_role("button", name="Uncheck All").click()
    #context.tracing.stop(path="trace1.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
