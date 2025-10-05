import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testing.qaautomationlabs.com/form.php")



    page.get_by_role("textbox", name="First Name:").click()
    page.get_by_role("textbox", name="First Name:").fill("test")
    page.get_by_role("textbox", name="Middle Name:").click()
    page.get_by_role("textbox", name="Middle Name:").fill("middle")
    page.get_by_role("textbox", name="Last Name:").click()
    page.get_by_role("textbox", name="Last Name:").fill("last name")
    page.get_by_role("textbox", name="Email:").click()
    page.get_by_role("textbox", name="Email:").fill("test@gmail.com")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Test@123")
    page.get_by_role("textbox", name="Address:").click()
    page.get_by_role("textbox", name="Address:").fill("bangalore")
    page.get_by_role("textbox", name="City:").click()
    page.get_by_role("textbox", name="City:").fill("bangalore")
    page.get_by_role("textbox", name="State:").click()
    page.get_by_role("textbox", name="State:").fill("karnataka")
    page.get_by_role("spinbutton", name="Pin Code:").click()
    page.get_by_role("spinbutton", name="Pin Code:").fill("560080")
    page.get_by_role("button", name="Submit").click()


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
