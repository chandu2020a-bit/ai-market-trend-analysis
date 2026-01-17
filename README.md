# AI-Based Market Trend Analysis and Demand Forecasting

This project implements an AI-based system to analyze market trends and forecast future demand using Google Trends data.

## Objective
To predict future market demand by learning patterns from historical consumer interest data using machine learning.

## Dataset
- Source: Google Trends
- Keyword: Walmart
- Region: United States
- Frequency: Weekly

## Methodology
- Data cleaning and time-series preparation
- Feature engineering using lag variables and rolling averages
- Model training using Random Forest Regression
- Evaluation using Mean Absolute Error (MAE)
- 8-week future demand forecasting

## Results
- Achieved MAE ≈ 3.23 on unseen test data
- Generated 8-week demand forecast with confidence band

## File Structure
- `notebooks/market_trend_analysis.ipynb` – Main notebook (primary evaluation artifact)
- `data/` – Dataset files
- `src/` – Supporting scripts

## Tools & Libraries
- Python
- Pandas
- Scikit-learn
- Matplotlib
