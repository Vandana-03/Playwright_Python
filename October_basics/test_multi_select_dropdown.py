from playwright.sync_api import Page

def test_drop_down(page: Page):
    page.goto("https://testing.qaautomationlabs.com/dropdown.php")

    #verify heading name
    page.get_by_title("Multi Selection Option",exact=True).is_visible()

    page.locator("#countryDropdown").select_option(value=["India", "UK"])

    #option 2
    page.locator("#countryDropdown").select_option(value="India", label="UK", index=4)
    page.wait_for_timeout(2000)

    #deselect the dropdown options
    page.locator("#countryDropdown").select_option()
    page.wait_for_timeout(2000)