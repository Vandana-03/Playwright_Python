from asyncio import wait_for

from playwright.sync_api import Page

#Get selected value from single Select dropdown| Assert dropdown value
def test_selected(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    # verify heading name
    page.get_by_title("Dropdown List").is_visible()
    page.wait_for_timeout(2000)

    page.get_by_role("checkbox", name="Please select an option").is_visible()
    page.locator("#dropdown").select_option("1")
    assert page.locator("#dropdown").input_value() == "1"
    page.wait_for_timeout(2000)
