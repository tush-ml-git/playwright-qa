import asyncio
from playwright.async_api import async_playwright
import re

seeds = range(33, 43)

async def main():
    total = 0
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for seed in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print(f"Processing {url}")
            
            await page.goto(url)
            await page.wait_for_selector("table")
            
            content = await page.content()
            numbers = re.findall(r'-?\d+\.?\d*', content)
            
            for num in numbers:
                total += float(num)
        
        await browser.close()
    
    print("FINAL TOTAL:", int(total))

asyncio.run(main())
