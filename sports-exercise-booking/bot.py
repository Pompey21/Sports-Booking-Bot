import os

from datetime import datetime, timedelta
from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv  # for python-dotenv method


def get_date_to_book():
    d = datetime.today() + timedelta(days=3)
    return d.date().day


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.sport.ed.ac.uk/online-booking/Account/LogOn
    page.goto("https://www.sport.ed.ac.uk/online-booking/Account/LogOn")
    # Click input[name="UserName"]
    page.click('input[name="UserName"]')
    # Fill input[name="UserName"]
    page.wait_for_timeout(1000)
    page.fill('input[name="UserName"]', os.environ.get("username", ""))
    # Press Tab
    page.press('input[name="UserName"]', "Tab")
    page.wait_for_timeout(1000)
    # Fill input[name="Password"]
    page.fill('input[name="Password"]', os.environ.get("password", ""))
    # Click input:has-text("Log on")
    page.click('input:has-text("Log on")')
    page.wait_for_timeout(1000)
    # assert page.url == "https://www.sport.ed.ac.uk/online-booking/"
    # Click #searchForClass
    page.click("#searchForClass")
    # Select 1
    page.select_option('select[name="SiteID"]', "1")
    # Select RP16
    page.select_option('select[name="Activity"]', "SWIM")
    # Click input[name="SearchDate"]
    page.wait_for_timeout(1000)
    page.click('input[name="SearchDate"]')
    # Click text=get_date_to_book()
    page.click(f"text={get_date_to_book()}")
    # Click input:has-text("Search")
    page.wait_for_timeout(1000)
    page.click('input:has-text("Search")')
    page.wait_for_timeout(1000)
    # assert page.url == "https://www.sport.ed.ac.uk/online-booking/Search/Results?site=1"
    page.click("id=basketControl_1_1")
    # assert page.url == "https://www.sport.ed.ac.uk/online-booking/Basket/ViewDetail"
    # Check input[name="TermsAccepted"]
    page.wait_for_timeout(1000)
    page.check('input[name="TermsAccepted"]')
    # Click input:has-text("Checkout")
    page.wait_for_timeout(1000)
    page.click('input:has-text("Checkout")')
    # assert page1.url == "https://www.sport.ed.ac.uk/online-booking-payment/"
    # Click text=Confirm your booking(s)
    page.wait_for_timeout(1000)
    page.click("text=Confirm your booking(s)")
    # assert page1.url == "https://www.sport.ed.ac.uk/online-booking-payment/Receipt?TransactionID=1081432&BasketId=f63fda27-ca17-479d-984f-0140e7d12d1e"
    # ---------------------
    context.close()
    browser.close()


def main():
    load_dotenv()
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    main()
