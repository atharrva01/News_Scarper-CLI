# News Scraper CLI

This is a simple command-line interface (CLI) tool that fetches the top 5 news articles based on a search query using the GNews API.

-----

## Features

  * **Quick News Access**: Get a summary of the top 5 news articles directly in your terminal.
  * **Customizable Queries**: Search for news on any topic you're interested in.
  * **Direct Links**: Each article comes with a URL to read the full story.

-----

## Getting Started

### Prerequisites

Before you run this script, make sure you have:

  * **Python 3.x** installed on your system.
  * The **`requests`** Python library. You can install it using pip:
    ```bash
    pip install requests
    ```

### API Key

This tool uses the [GNews API](https://gnews.io/). You'll need an **API key** to use it. The current script has a placeholder key. **It's highly recommended to replace `api` with your own API key** to avoid rate limits and ensure consistent access.

### Installation

1.  **Save the Code**: Save the provided Python code into a file named, for example, `news_scraper.py`.

-----

## Usage

To fetch news, open your terminal, navigate to the directory where you saved `news_scraper.py`, and run the script with the `--query` argument:

```bash
python news_scraper.py --query "your news topic here"
```

**Examples:**

```bash
python news_scraper.py --query artificial intelligence
python news_scraper.py --query climate change initiatives India
```

### Command-Line Arguments

  * `--query` (required): This is where you enter your search terms for news articles. If your query contains spaces, remember to enclose it in double quotes (`"`).

-----

## Output

The script will display the top 5 news articles, showing the title, description, a direct link to the article, and when it was published.

**Example Output:**

```
Here are your Top 5 news: 

The Title of the news is, Scientists Discover New Species in Amazon Rainforest

The description: 
Researchers have identified a previously unknown frog species during an expedition.

If you want to read the full article visit 
https://example.com/amazon-frog-discovery

This article is published at 
2025-07-29T12:00:00Z

The Title of the news is, Global Markets React to Latest Economic Data
... (and so on for up to 5 articles)
```

If no articles are found for your query, you'll see:

```
❌ No news articles found for this query.
```
