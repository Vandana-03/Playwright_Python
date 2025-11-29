from asyncio import wait_for

import pytest
from playwright.sync_api import Page

@pytest.mark.parametrize("username,password",
                         [ ("standard_user","secret_sauce"),
                           ("locked_out_user","secret_sauce"),
                           ("problem_user","secret_sauce"),
                           ("performance_glitch_user","sdsdsewwdasd")
                         ])
def test_launch(page: Page,username,password)-> None:
    page.goto("https://www.saucedemo.com/v1/")
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").dblclick()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.get_by_role("button", name="LOGIN").click()
    page.wait_for_timeout(2000)
