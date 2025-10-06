from playwright.sync_api import Page

def test_radio_buttons(page: Page):
    page.goto("https://testing.qaautomationlabs.com/radio-button.php")
    #verify heading name
    page.get_by_role("heading", name="Radio Button Demo").is_visible()

    #verify title name
    page.get_by_text("Click on button to get the selected value.",exact=True).is_visible()

    # select male
    page.get_by_role("radio", name="Male").first.check()
    page.get_by_role("button", name="Show Selected Gender").click()
    page.get_by_text("You selected: Male",exact=True).is_visible()

    #select female
    page.get_by_text("Female").first.click()
    page.get_by_role("button", name="Show Selected Gender").click()
    page.get_by_text("You selected: Female", exact=True).is_visible()


    #section 2
    page.get_by_text("Radio Button 1").check()
    page.get_by_text("Radio Button 2").check()
    page.locator("label").filter(has_text="Disabled Radio Button").is_disabled()

    #section 3
    page.get_by_text("Click on button to get the selected values from Gender and Age",exact=True).is_visible()
    page.get_by_text("Male").nth(3).check()
    page.get_by_role("button", name="Show Selected Values").click()
    page.get_by_text("Female").nth(1).click()
    page.get_by_role("button", name="Show Selected Values").click()
    page.get_by_text("Please select both gender and").click()
    page.get_by_text("Under").click()
    page.get_by_text("-35").click()
    page.get_by_text("+").click()
    page.get_by_role("button", name="Show Selected Values").click()

