from playwright.sync_api import Playwright, sync_playwright, expect

email = ["1","2","3"]
code = ["1"]

# for i in email:

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.youtube.com/")
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill("testing")
    page.get_by_placeholder("Search").press("Enter")
    page.get_by_placeholder("Search").click()
    page.get_by_placeholder("Search").fill("end")
    page.get_by_placeholder("Search").press("Enter")

    for i in email:
        page.get_by_placeholder("Search").click()
        page.get_by_placeholder("Search").fill(i)
        page.get_by_placeholder("Search").press("Enter")

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
