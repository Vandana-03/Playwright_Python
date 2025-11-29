from pathlib import Path
import re
import pytest
from playwright.sync_api import Page
from slugify import slugify

#Attach Screenshot in Pytest HTML Report on Failure with Playwright

def test_drop_down(page: Page):
    page.goto("https://testing.qaautomationlabs.com/dropdown.php")
    #verify heading name

    page.get_by_title("Dropdown Demo").is_visible()

    page.locator("#fruitDropdown").select_option("Apple")
    page.get_by_text("You selected: Apple").click()
    page.locator("#fruitDropdown").select_option("Banana")
    page.locator("#fruitDropdown").select_option("Mango")
    page.locator("#fruitDropdown").select_option("Orange")
    page.locator("#fruitDropdown").select_option("M Orange")

#Code snippet attaching Screenshots:
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if report.failed or xfail and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=screen_file)

        if (report.skipped and xfail) or (report.failed and not xfail):
            #add the screenshots to the html report
            extra.append(pytest_html.extras.png(screen_file))
        report.extra = extra
