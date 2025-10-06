from playwright.sync_api import Page

def test_drop_down(page: Page):
    page.goto("https://testing.qaautomationlabs.com/dropdown.php")
    #verify heading name

    page.get_by_title("Dropdown Demo").is_visible()

    page.locator("#fruitDropdown").select_option("Apple")
    page.get_by_text("You selected: Apple").click()
    page.locator("#fruitDropdown").select_option("Banana")
    page.locator("#fruitDropdown").select_option("Mango")
    page.locator("#fruitDropdown").select_option("Orange")


'''does not work → Playwright only supports passing a list if the <select> allows multiple selections'''
    #page.locator("#fruitDropdown").select_option(value=["Apple", "Banana", "Mango", "Orange"])