# Data Collection and Feature Engineering

This repository contains Python code to scrape financial data for S&P 500 companies, perform feature engineering to compute important financial metrics, and use those metrics to select a portfolio of stocks for investment.

## Getting Started

The first step in this project is to obtain a list of the S&P 500 stock names. We obtained this list from the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) and used the `beautifulsoup4` package to parse the HTML and extract the relevant information.

Next, we wrote a function to scrape financial data for each stock using the [stockanalysis.com](https://stockanalysis.com/) website. Specifically, we scraped data for the income statement, balance sheet, cash flow statement, and ratios tables. We used the `requests` and `beautifulsoup4` packages for web scraping.

After obtaining the financial data, we performed feature engineering to compute important financial metrics. These metrics included the cash ratio, Quick ratio, inventory turnover, D/C ratio (Debt to capital ratio), Receivables turnover, Return on assets (ROA), and ROE.

Finally, we used these metrics to select a portfolio of stocks for investment.

## References

The list of S&P 500 companies was obtained from the [Wikipedia page](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).

Financial data was scraped from [stockanalysis.com](https://stockanalysis.com/) using the `requests` and `beautifulsoup4` packages.
