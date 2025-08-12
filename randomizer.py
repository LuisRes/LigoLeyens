from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://l-randomizer.vercel.app")

    # Click the generate button
    page.click("text=Randomize")

    # Wait for the build to appear
    page.wait_for_selector(".result-wrapper")

    # Get the generated text
    build_html = page.inner_text(".result-wrapper")

    print("Random Build:\n", build_html)

    browser.close()