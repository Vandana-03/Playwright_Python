from playwright.sync_api import Playwright, sync_playwright, expect

def fileupload(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=90)
    context = browser.new_context()
    page=context.new_page()
    page.goto("https://testing.qaautomationlabs.com/file-upload.php")

    #check the page title
    page.get_by_role("heading",name="File Upload Demo").highlight()

    #store the file path in a variable
    file_path="C:\\Vandana\\Python\\Playwright_Demo_July\\testdata\\File1.txt"

    #select the browse button and upload
    page.set_input_files("//label[@class='file-label']", file_path)
    page.locator("#fileInfo").is_visible()

    #print the success message after uploading the file
    print(page.locator("#fileInfo").text_content())

with sync_playwright() as playwright:
    fileupload(playwright)