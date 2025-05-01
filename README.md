# IMDb Scraper Project 🎬

A Python-based automated scraper that extracts and organizes data from IMDb, using robust Object-Oriented Programming (OOP) principles and Selenium WebDriver.

##  Features
- Scrapes the Top 15 Most Popular Movies and their Trivia.
- Scrapes Upcoming Movies categorized by release date.
- Scrapes Top News headlines from IMDb.
- Outputs clean, structured data into a multi-sheet Excel file (`imdb_data.xlsx`).
- Built with solid error handling to ensure reliability.
- Designed with modular OOP architecture for easy maintenance and scalability.
- Headless browser operation for efficient background scraping.

## Technologies Used
- **Selenium** (web scraping automation)
- **Pandas** (data processing)
- **OpenPyXL** (Excel output)

## Requirements
- Python
- Google Chrome browser installed
- Compatible ChromeDriver version

## Project Structure
```bash
├── data/                     
│   ├── imdb_data.xlsx         
│   ├── popular_movies_data.csv
│   ├── top_news_data.csv
│   └── upcoming_movies_data.csv
│
├── scraper/                  
│   ├── base_scraper.py       
│   ├── popular_movies.py     
│   ├── top_news.py           
│   └── upcoming_movies.py    
│
├── main.py                   
├── requirements.txt          
└── README.md                 
```

## How to Run
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the project:
    ```bash
    python main.py
    ```
   
The scraper will generate `imdb_data.xlsx` with three sheets:
- Popular Movies
- Upcoming Movies
- Top News

## Possible Extensions
- Optional: Automated scheduling (e.g., cron jobs or Task Scheduler).
- Database integration (SQLite/PostgreSQL).
- Data visualization (Matplotlib, Seaborn).
- Adding command-line interface (argparse).

## About This Project
This project demonstrates strong skills in:
- Browser automation and dynamic content scraping,
- Object-oriented software design,
- Data wrangling and structured reporting,
- Error handling and fault-tolerant coding practices.

## License
This project is for educational and portfolio purposes.

---

> **Built with focus on clean code, scalability, and real-world applicability.**

