from playwright.sync_api import Playwright, expect, sync_playwright

def dragdrop(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=9000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    src=page.locator("#column-a")
    destination=page.locator("#column-b")

    src.drag_to(destination)
    expect(destination).to_have_text("A")
    expect(src).to_have_text("B")

    #below commented code doesnt work
    '''page.locator("src").hover()
    page.mouse.down()
    page.locator("destination").hover()
    page.mouse.up()'''

    context.close()
    browser.close()

with sync_playwright() as playwright:
    dragdrop(playwright)



