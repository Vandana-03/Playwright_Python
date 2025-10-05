from playwright.sync_api import Playwright, sync_playwright, expect

def move_slider(page, handle_selector: str, value_selector: str, offset_x: int, expected_value: str):
    handle = page.locator(handle_selector)
    handle.drag_to(handle, target_position={"x": offset_x, "y": 0})

    value_text = page.locator(value_selector).inner_text()
    print(f"Displayed value after moving {offset_x}px:", value_text)

    assert expected_value in value_text, f"Expected value {expected_value} but got {value_text}"


def slider(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=200)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testing.qaautomationlabs.com/slider.php")

    page.get_by_role("heading", name="Slider Demo").is_visible()
    page.get_by_text("Default value 10").is_visible()

    #slider1
    move_slider(page, "#slider1", "#value1", 200, "76")  # move right
    move_slider(page, "#slider1", "#value1", 10, "0")  # move back left

    # slider2
    move_slider(page, "#slider2", "#value2", 100, "34")  # move right
    move_slider(page, "#slider2", "#value2", 20, "0")  # move back left

    # slider3
    move_slider(page, "#slider3", "#value3", 200, "76")  # move right
    move_slider(page, "#slider3", "#value3", 25, "2")  # move back left

    # slider4
    move_slider(page, "#slider4", "#value4", 210, "80")  # move right
    move_slider(page, "#slider4", "#value4", 30, "4")  # move back left

    # slider5
    move_slider(page, "#slider5", "#value5", 220, "84")  # move right
    move_slider(page, "#slider5", "#value5", 40, "8")  # move back left

    # slider6
    move_slider(page, "#slider6", "#value6", 250, "97")  # move right
    move_slider(page, "#slider6", "#value6", 50, "12")  # move back left

    context.close()
    browser.close()

with sync_playwright() as playwright:
    slider(playwright)