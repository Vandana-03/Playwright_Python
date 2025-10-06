from playwright.sync_api import sync_playwright, Playwright, expect


def listbox(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testing.qaautomationlabs.com/list-box.php")

    #verify title
    page.get_by_role("heading", name="List Box Demo").click()

    #verify Heading name
    page.locator("section").get_by_text("List Box", exact=True).click()

    names = ["Sakshi", "Mayra", "Sanjana","Riyanshi","Ryan","Mohit"]

    for name in names:
        page.locator("#list1").select_option(name)
        page.get_by_role("button", name="Add", exact=True).click()


    page.get_by_role("button", name="Add All").click()
    expect(page.locator("#list1")).to_be_empty()

    page.locator("#list2").select_option("Sakshi")
    page.get_by_role("button", name="Remove", exact=True).click()
    page.locator("#list2").select_option("Sanjana")
    page.get_by_role("button", name="Remove", exact=True).click()
    page.locator("#list2").select_option("Niken")
    page.get_by_role("button", name="Remove", exact=True).click()
    page.locator("#list2").select_option("Yashika")
    page.get_by_role("button", name="Remove", exact=True).click()
    page.get_by_role("button", name="Remove All").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    listbox(playwright)
