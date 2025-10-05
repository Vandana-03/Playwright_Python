import os

from playwright.sync_api import Playwright, sync_playwright, expect

def filedownload(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=900)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_i:
        page.get_by_text("file_1759591910480.pdf").click()
    download=download_i.value

    current_working_dir=os.getcwd()
    final_path=os.path.join(current_working_dir,"testdata/")
    download.save_as(final_path + download.suggested_filename)

with sync_playwright() as playwright:
    filedownload(playwright)