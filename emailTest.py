import emailList;

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1687185951&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26nlp%3d1%26RpsCsrfState%3d6332f5d4-d145-8f1a-cc4c-647ce941a769&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")
    page.get_by_placeholder("Email, phone, or Skype").click()
    page.get_by_placeholder("Email, phone, or Skype").fill(emailList.myEmail)
    page.get_by_role("button", name="Next").click()
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(emailList.myPassword)
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Yes").click()

    n = len(emailList.emails)

    for i in range(n):
        page.get_by_role("button", name="New mail").get_by_role("button", name="New mail", exact=True).filter(has_text="New mailNew mail (N) Create a new email message.").click()
        page.get_by_role("textbox", name="To", exact=True).click()
        page.get_by_role("textbox", name="To", exact=True).fill(emailList.emails[i])
        page.get_by_role("textbox", name="To", exact=True).press("Enter")
        page.get_by_placeholder("Add a subject").click()
        page.get_by_placeholder("Add a subject").fill("This is a test")
        page.get_by_role("textbox", name="Message body, press Alt+F10 to exit").locator("div").click()
        page.get_by_role("textbox", name="Message body, press Alt+F10 to exit").fill(emailList.codes[i])
        page.get_by_title("Send (Ctrl+Enter)").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)