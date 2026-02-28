import asyncio
from playwright.async_api import async_playwright

seeds = range(33, 43)

async def main():
    total = 0
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        for seed in seeds:
            url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
            print("Processing:", url)
            
            await page.goto(url)
            
            # Wait for table fully loaded
            await page.wait_for_selector("table")
            
            # Extract numbers from table cells
            cells = await page.query_selector_all("td")
            
            for cell in cells:
                text = await cell.inner_text()
                text = text.strip()
                
                try:
                    number = float(text)
                    total += number
                except:
                    pass
        
        await browser.close()
    
    print("FINAL TOTAL:", int(total))

asyncio.run(main())
