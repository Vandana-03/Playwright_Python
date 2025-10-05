from playwright.sync_api import Playwright, expect, sync_playwright


#this code is not working properly not sure of what the issue is

def notifications(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=900)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testing.qaautomationlabs.com/notifications.php")
    # Ensure the heading is present
    page.get_by_role("heading",name="Notification Demo").highlight()

    # Success Message
    page.get_by_role("button", name="Success Message").click()
    page.get_by_text("Notification Body:- You Notification Body Goes Here.").is_visible()
    page.get_by_role("button", name="Close").first.click()

    page.get_by_role("button",name="Info Message").click()
    page.get_by_text("Notification Body:- You Notification Body Goes Here.").is_visible()
    page.get_by_role("button", name="Close").nth(1).click()

   
    page.get_by_role("button",name="Primary Message").click()
    page.get_by_text("Notification Body:- You Notification Body Goes Here.")
    page.get_by_role("button", name="Close").nth(2).click()

    page.get_by_role("button", name="Error Message").click()
    page.get_by_text("Notification Body:- You Notification Body Goes Here.").is_visible()
    page.get_by_role("button", name="x").nth(3).click()




    context.close()
    browser.close()




with sync_playwright() as playwright:
    notifications(playwright)