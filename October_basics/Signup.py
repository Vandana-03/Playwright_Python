from time import localtime

from playwright.sync_api import Playwright, sync_playwright, expect


def signup(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False,slow_mo=900)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://testing.qaautomationlabs.com/form.php")

    page.locator("#firstname").fill("testfirstname") #xpath with id
    page.locator("#middlename").fill("testmiddlename")  #xpath with id
    page.locator("#lastname").fill("testlastname") #xpath with id
    page.locator("//input[@id='email']").fill("test@gmail.com")
    page.locator("//input[@id='password']").fill("test@123")
    page.locator("//textarea[@id='address']").fill("house 22,10th cross delhi")
    page.locator("#city").fill("chandini chowk")
    page.locator("#states").fill("New delhi")
    page.locator("#pincode").type("560801")
    page.get_by_role("button", name="Submit").click()
    # Wait for success message and assert
    page.wait_for_selector(".text-success.mt-3.font-weight-bold")
    expect(page.locator(".text-success.mt-3.font-weight-bold")).to_contain_text("Form submitted successfully")

    context.close()
    browser.close()


with sync_playwright() as playwright:
    signup(playwright)