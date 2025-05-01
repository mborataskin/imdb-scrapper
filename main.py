from scraper.popular_movies import PopularMoviesScraper
from scraper.upcoming_movies import UpcomingMoviesScraper
from scraper.top_news import TopNewsScraper

if __name__ == "__main__":
    print("Program started. Scraping data from IMDb, please wait...")

    popular = PopularMoviesScraper()
    popular.scrape()

    upcoming = UpcomingMoviesScraper()
    upcoming.scrape()

    news = TopNewsScraper()
    news.scrape()

    news.remove_placeholder_sheet()
    news.quit()