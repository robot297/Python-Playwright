import re
from playwright.sync_api import Page, expect

from pom.loginpage import LoginPage

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_sauce_demo_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.send_username("standard_user")
    login_page.send_password("secret_sauce")
    login_page.login_click()

    # Expect the URL to contain "inventory.html".
    expect(page).to_have_url(re.compile(".*inventory.html"))
