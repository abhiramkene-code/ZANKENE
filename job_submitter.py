from playwright.sync_api import sync_playwright
import os
import time

class UpworkJobSubmitter:
    def __init__(self):
        self.user_data_dir = os.path.join(os.path.expanduser("~"), "zankene_edge_profile")

    def open_and_fill_proposal(self, job_url: str, proposal_text: str):
        print(f"\n?? [AUTO-SUBMITTER] Opening Edge for: {job_url}")
        with sync_playwright() as p:
            try:
                browser = p.chromium.launch(
                    channel="msedge",
                    headless=False,
                    args=["--disable-blink-features=AutomationControlled"]
                )
                context = browser.new_context(
                    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/120.0.0.0 Safari/537.36"
                )
                page = context.new_page()

                print(f"?? Navigating directly to: {job_url}")
                page.goto(job_url, wait_until="domcontentloaded", timeout=60000)
                print("?? Page loaded! Checking for Apply / Submit buttons...")
                time.sleep(5)

                apply_btn = page.locator("a:has-text('Apply Now'), button:has-text('Apply Now'), a:has-text('Submit a Proposal')").first
                if apply_btn.is_visible():
                    print("? Clicking 'Apply Now / Submit Proposal'...")
                    apply_btn.click()
                    time.sleep(5)

                cover_letter_box = page.locator("textarea#cover-letter, textarea[aria-label*='Cover Letter'], textarea").first
                if cover_letter_box.is_visible():
                    print("?? Auto-filling generated proposal text...")
                    cover_letter_box.fill(proposal_text)
                    print("? Proposal text injected into Cover Letter field!")
                else:
                    print("?? If login prompt appears, please log in inside this window.")

                print("? Keeping Edge open for 60 seconds...")
                time.sleep(60)
                browser.close()
            except Exception as e:
                print(f"?? Auto-submit notice: {e}")

if __name__ == "__main__":
    submitter = UpworkJobSubmitter()
    test_url = "https://www.upwork.com/jobs/Python-Automation-Script-Excel-CSV-Data-Processing_~022102452385220593190/"
    test_proposal = "Hi there,\n\nI can build this automation using Pandas/Playwright immediately.\n\nBest,\nAbhiram P."
    submitter.open_and_fill_proposal(test_url, test_proposal)
