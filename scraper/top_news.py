from scraper.base_scraper import BaseScraper
from selenium.webdriver.common.by import By
import pandas as pd

class TopNewsScraper(BaseScraper):
    def scrape(self):
        try:
            self.driver.get("https://www.imdb.com/news/top/")
            top_news = self.driver.find_elements(By.CSS_SELECTOR, "div[data-testid='item-id']")

            top_news_data = []

            for article in top_news[:15]:
                try:
                    title = article.find_element(By.CSS_SELECTOR, ".ipc-link.ipc-link--base").text
                except:
                    title = "N/A"

                try:
                    index = article.find_element(By.CSS_SELECTOR, ".ipc-html-content-inner-div").text.strip().split("\n")[0]
                except:
                    index = "-"

                try:
                    date_elements = article.find_elements(By.CSS_SELECTOR, ".ipc-inline-list__item")
                    date = date_elements[0].text if date_elements else "Unknown"
                except:
                    date = "Unknown"

                try:
                    link = article.find_element(By.CSS_SELECTOR, ".ipc-link--base.sc-c09843a2-0.kEQUaW").get_attribute("href")
                except:
                    link = "-"

                top_news_data.append({
                    "Article ID": len(top_news_data) + 1,
                    "Title": title,
                    "Index": index,
                    "Date": date,
                    "Full Article Link": link
                })

            df = pd.DataFrame(top_news_data)
            df.to_csv("data/top_news_data.csv", index=False)

            try:
                with pd.ExcelWriter("data/imdb_data.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                    df.to_excel(writer, sheet_name="Top News", index=False)
            except Exception as e:
                print(f"Error while writing to Excel file: {e}")

            print("Top News saved successfully.")

        except Exception as e:
            print(f"TopNewsScraper error: {e}")
