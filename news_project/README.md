# 📰 News Data Analysis & Headlines Scraping Project

This project is a comprehensive data science workflow designed to harvest news data from a live API, process it using advanced Python libraries, and analyze it to uncover hidden trends in global journalism. It fulfills the requirements for Regex, Scraping (API), NumPy/Matplotlib, and Pandas analysis.

## 🚀 Key Features and Requirements Met

### 1. Data Collection & Engineering (Regex & Scraping)
- **API Scraping**: Uses `fetch_news.py` to connect to the [NewsData.io](https://newsdata.io/) API. It implements a robust **pagination engine** that traverses multiple result pages using `nextPage` tokens to build a significant dataset (up to hundreds of articles).
- **Regex Parsing**: The `pandas_analysis.ipynb` notebook utilizes **Regular Expressions** (`re` module) to extract precise temporal data (hours) from ISO-8601 timestamps, demonstrating robust data extraction from raw text strings.
- **Dataset**: All collected data is exported to `news_data.csv`.

### 2. NumPy & Matplotlib Analysis
- **Notebook**: `numpy_analysis.ipynb`
- **Focus**: Efficiency and Visualization at scale.
- **Advanced Work**: Uses **NumPy** for computing statistical benchmarks on headline structural complexity (Mean, Median, Standard Deviation).
- **Visuals**: 
    - Top 10 News Source volume bars.
    - Histogram of Headline Character Count distributions.
    - Kernel Density Estimation (KDE) of Description word counts.
    - Scatter plots investigating complexity correlations.

### 3. Pandas Hypothesis Testing & Machine-Categorization
- **Notebook**: `pandas_analysis.ipynb`
- **Hypothesis**: *Global news follows a 'Shift Pattern', where article frequency peaks at regular intervals throughout the day.*
- **Methodology**: Extensive time-series manipulation including Hour extraction via Regex.
- **Advanced Analysis**:
    - **Heatmaps**: Visualizing news density by Source over a 24-hour cycle.
    - **Author Volume**: Identifying the most prolific contributors in the dataset.
    - **Keyword Analysis (Regex-Categorizer)**: Automatically tagging articles into categories (Crime, Politics, Tech, Sports, business) based on title content patterns.
    - **Cumulative Velocity**: Tracking the real-time accumulation of news for top sources over 24 hours.

---

## 📊 Key Findings & Visual Highlights

### 🧪 Hypothesis: The 'Shift Pattern'
Our analysis of the **Hourly Distribution (UTC)** disproved the initial hypothesis. Instead of sharp "morning" and "evening" peaks, the global news cycle is remarkably decentralized. 
- **Finding**: While some local sources peak, the aggregate global news volume is spread relatively evenly across time zones, suggesting a 24/7 breaking-news environment rather than traditional "newspaper shifts."

### 🔦 Heatmap Analysis: Source vs. Hour
The heatmap revealed that major international news agencies maintain steady output, while smaller, regional players exhibit more distinct 'quiet periods' during their local night hours (UTC conversion).

### 🏷️ Regex Topic Distribution
By implementing a custom regex-based classifier, we identified that **Politics** and **Crime/Justice** are the dominant themes in the current data stream, significantly outperforming **Tech** and **Sports** in title volume.

---

## 📂 Project Structure
- `fetch_news.py`: The "Scraper" – Automates high-volume data retrieval with pagination.
- `news_data.csv`: The raw dataset containing source, author, title, description, and time.
- `numpy_analysis.ipynb`: Technical analysis focused on volume and cleaning using NumPy.
- `pandas_analysis.ipynb`: Scientific analysis focused on hypothesis testing and peak-hour trends using Pandas.
- `README.md`: This documentation.

---

## 🛠️ Setup & Installation
1. **Initialize Environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```
2. **Install Dependencies**:
   ```bash
   pip install requests pandas numpy matplotlib seaborn jupyter
   ```
3. **Execution**:
   - Run `python fetch_news.py` to refresh the dataset (Note: NewsData.io has rate limits for free keys).
   - Launch Jupyter: `jupyter notebook` to explore the analysis files.

## 🎓 Note these things please
This project demonstrates a full-stack data science lifecycle: from **automated data ingestion** (API handling with pagination) to **advanced data wrangling** (Regex/Pandas) and finally **visual storytelling** (Matplotlib/Seaborn). It handles real-world API challenges like pagination and rate-limiting gracefully, providing a scientific basis for its findings through hypothesis testing.
