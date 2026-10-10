from playwright.sync_api import sync_playwright
import time
import re

class UpworkJobScanner:
    def __init__(self, keywords=["python automation", "ai agent"]):
        self.keywords = keywords

    def clean_text(self, text: str) -> str:
        clean = re.sub(r"<[^>]+>", "", text)
        return clean.strip()

    def clean_url(self, url: str) -> str:
        # URL-? ?????? HTML ????? ?????? ?????? ??????????
        clean_link = re.sub(r"span-class-highlight-", "", url)
        clean_link = re.sub(r"-span", "", clean_link)
        return clean_link

    def fetch_live_jobs(self) -> list:
        jobs = []
        print("?? [PLAYWRIGHT SCRAPER] Scanning jobs using Local Chrome...")
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(channel="chrome", headless=True)
            except Exception:
                browser = p.chromium.launch(channel="msedge", headless=True)

            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = context.new_page()

            for keyword in self.keywords:
                search_url = f"https://www.upwork.com/nx/search/jobs/?q={keyword.replace(' ', '%20')}"
                try:
                    page.goto(search_url, wait_until="domcontentloaded", timeout=30000)
                    time.sleep(3)
                    job_tiles = page.locator("article").all()
                    for tile in job_tiles[:3]:
                        title_element = tile.locator("a").first
                        if title_element:
                            raw_title = title_element.inner_text()
                            title = self.clean_text(raw_title)
                            
                            raw_link = title_element.get_attribute("href")
                            if raw_link:
                                if not raw_link.startswith("http"):
                                    raw_link = "https://www.upwork.com" + raw_link
                                link = self.clean_url(raw_link)
                                jobs.append({"title": title, "link": link, "keyword": keyword})
                except Exception as e:
                    print(f"?? Fetch error for '{keyword}': {e}")
            browser.close()
        return jobs

if __name__ == "__main__":
    scanner = UpworkJobScanner()
    found_jobs = scanner.fetch_live_jobs()
    print(f"? Scraped {len(found_jobs)} active jobs.")
    for idx, job in enumerate(found_jobs, 1):
        print(f"\n[{idx}] {job['title']}\n    Link: {job['link']}")
