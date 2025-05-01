from scraper.base_scraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class PopularMoviesScraper(BaseScraper):
    def scrape(self):
        try:
            self.driver.get("https://www.imdb.com/chart/moviemeter/")
            popular_movies = self.driver.find_elements(By.CSS_SELECTOR, ".ipc-title-link-wrapper")
            movie_links = [movie.get_attribute("href") for movie in popular_movies[:15]]

            data = []

            for link in movie_links:
                try:
                    self.driver.get(link)
                except Exception as e:
                    print(f"Failed to load the page: {link} - {e}")
                    continue

                try:
                    original_title_element = self.driver.find_element(By.XPATH,
                                                                      "//div[contains(text(), 'Original title:')]")
                    title = original_title_element.text.replace("Original title: ", "")
                except:
                    try:
                        title = self.driver.find_element(By.CSS_SELECTOR, ".hero__primary-text").text
                    except:
                        title = "N/A"

                try:
                    trivia_link = WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.LINK_TEXT, "Trivia")))
                    trivia_link.click()
                    trivia_elements = WebDriverWait(self.driver, 4).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ipc-html-content-inner-div"))
                    )
                    trivia_list = [trivia.text for trivia in trivia_elements[:3]]
                    while len(trivia_list) < 3:
                        trivia_list.append("-")
                except:
                    trivia_list = ["-"] * 3

                data.append({
                    "Popularity": len(data) + 1,
                    "Movie Title": title.split(" (")[0],
                    "Trivia 1": trivia_list[0],
                    "Trivia 2": trivia_list[1],
                    "Trivia 3": trivia_list[2],
                })

            df = pd.DataFrame(data)
            df.to_csv("data/popular_movies_data.csv", index=False)
            try:
                with pd.ExcelWriter("data/imdb_data.xlsx", engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
                    df.to_excel(writer, sheet_name="Popular Movies", index=False)
                print("Popular Movies saved successfully.")
            except Exception as e:
                print(f"Error while writing to Excel file: {e}")

        except Exception as e:
            print(f"PopularMoviesScraper error: {e}")