from playwright.async_api import async_playwright

async def get_build_async(role: str, champ: str) -> bytes:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(locale='es-ES')
        page = await context.new_page()
        await page.goto("https://l-randomizer.vercel.app")

        target_div = page.locator(
            '.flex.flex-wrap.w-9\\/12.max-w-\\[1200px\\].justify-evenly.md\\:max-lg\\:justify-center'
        )    

        role_selected = page.get_by_alt_text(f"Role {role}")
        
        await page.get_by_placeholder("Search Champions").fill(champ)
        await page.get_by_placeholder("Select role").fill(role)
        await page.get_by_role('button', name='Randomize').click()

        old_alt = await role_selected.get_attribute("alt")
        await page.wait_for_function(
            "(el, oldAlt) => el !== oldAlt",
            arg=[role_selected, old_alt]
        )

        build = await target_div.screenshot()

        await page.pause()

        await context.close()
        await browser.close()

        return build