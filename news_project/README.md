# News API Data Analysis Project

This project fetches top U.S. headlines from the [News API](https://newsapi.org/), parses the data, saves it as a CSV dataset, and visualizes it using Pandas, NumPy, and Matplotlib.

## File Structure
- `fetch_news.py`: Script to connect to the News API and download data into `news_data.csv`.
- `news_data.csv`: (Generated after running script) Raw dataset.
- `numpy_analysis.ipynb`: Analyzes dataset cleanly displaying sources grouping with NumPy and Matplotlib.
- `pandas_analysis.ipynb`: Explores variables dynamically with Pandas, implementing Regex parsing of time logs, and tests an article publishing distribution hypothesis. 

## Requirements
Please ensure you setup your virtual environment and install the correct modules:
```bash
python -m venv venv
venv\Scripts\activate
pip install requests pandas numpy matplotlib jupyter
```

Then remember to replace `YOUR_API_KEY_HERE` inside `fetch_news.py` before executing!
