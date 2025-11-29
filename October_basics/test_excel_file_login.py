import csv
from asyncio import wait_for
from operator import truediv

import pytest
from playwright.sync_api import Page


def get_csv_data():
    data=[]
    with open("./testdata/login_cred.csv", "r",encoding="utf-8") as file:
        reader=csv.reader(file)
        #next(reader)  # skip header row
        for row in reader:
            data.append(row)
    return data

@pytest.mark.parametrize("username,password", get_csv_data())
def test_launch_login(page: Page,username,password)-> None:
    page.goto("https://www.saucedemo.com/v1/")
    page.get_by_text("Accepted usernames are: standard_user locked_out_user problem_user").dblclick()
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.get_by_role("button", name="LOGIN").click()
    page.wait_for_timeout(2000)



