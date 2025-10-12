from playwright.sync_api import Page

def test_drop_down(page: Page):
    page.goto("https://google.com")

    #print page source on console
    #print(page.content())


    page_source = page.content()
    with open("page_source.txt", "w", encoding="utf-8") as f:
        f.write(page_source)
    # Optionally, print confirmation
    print("Page source saved to page_source.txt")
