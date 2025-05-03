# --- config.py ---
# Configuration settings

WEBULL_EMAIL = "your_email@example.com"
WEBULL_PASSWORD = "your_password"
MFA_CODE = "your_mfa_code_if_needed"

PROFIT_TARGET = 0.5  # 50% gain
STOP_LOSS = 0.3      # 30% loss

SPY_SYMBOL = "SPY"
OPTION_EXPIRY_DAYS = 7  # Choose options 1 week out

MODEL_PATH = "model.pkl"

NEWS_SOURCES = [
    "https://www.cnbc.com/world/?region=world",
    "https://finance.yahoo.com/"
]

# For scraping, set user-agent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36"
}


# --- scraper.py ---
# News scraper and sentiment analyzer

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import config

def scrape_headlines():
    headlines = []
    for url in config.NEWS_SOURCES:
        r = requests.get(url, headers=config.HEADERS)
        soup = BeautifulSoup(r.content, "html.parser")
        for tag in soup.find_all("h2"):
            if tag.text.strip():
                headlines.append(tag.text.strip())
    return headlines

def analyze_sentiment(headlines):
    polarity = 0
    for headline in headlines:
        analysis = TextBlob(headline)
        polarity += analysis.sentiment.polarity
    avg_sentiment = polarity / len(headlines) if headlines else 0
    return avg_sentiment


# --- features.py ---
# Technical indicator calculator

import pandas as pd
import ta


def compute_features(df):
    df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    df["ma_50"] = ta.trend.SMAIndicator(df["close"], window=50).sma_indicator()
    df["ma_200"] = ta.trend.SMAIndicator(df["close"], window=200).sma_indicator()
    df = df.dropna()
    return df


# --- model.py ---
# ML Model: train and predict

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def train_model(df):
    df["target"] = (df["close"].shift(-1) > df["close"]).astype(int)
    X = df[["rsi", "ma_50", "ma_200"]]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    joblib.dump(model, config.MODEL_PATH)

    score = model.score(X_test, y_test)
    print(f"Model test accuracy: {score:.2f}")


def load_model():
    return joblib.load(config.MODEL_PATH)


def predict(model, latest_features):
    return model.predict([latest_features])[0]


# --- trading.py ---
# Webull Trading Handler

from webull import paper_webull
import config

wb = paper_webull()


def login_webull():
    wb.login(username=config.WEBULL_EMAIL, password=config.WEBULL_PASSWORD, mfa=config.MFA_CODE)


def find_spy_option():
    options = wb.get_options(config.SPY_SYMBOL)
    # (simplify: assume we pick the nearest expiry call/put ATM)
    # NOTE: production needs better selection logic!
    return options["call"] if options else None


def place_order(option_id, action="BUY", price=None, qty=1):
    wb.place_option_order(
        option_id=option_id,
        action=action,
        order_type="LMT" if price else "MKT",
        price=price,
        enforce="GTC",
        qty=qty
    )

# --- backtest.py ---
# Simple Backtesting Module

import matplotlib.pyplot as plt

def backtest(df, model):
    profits = []

    for i in range(1, len(df)):
        features = df.iloc[i][["rsi", "ma_50", "ma_200"]].values
        prediction = predict(model, features)

        if prediction == 1:  # Buy
            entry = df.iloc[i].close
            exit_price = df.iloc[i + 1].close if i + 1 < len(df) else entry
            profit = (exit_price - entry) / entry
            profits.append(profit)

    cumulative = (pd.Series(profits) + 1).cumprod()
    cumulative.plot()
    plt.title("Backtest Equity Curve")
    plt.show()

    print(f"Total return: {(cumulative.iloc[-1] - 1) * 100:.2f}%")


# --- main.py ---
# Master runner

import scraper
import features
import model
import trading
import config
import pandas as pd

def run():
    # 1. Login
    trading.login_webull()

    # 2. Scrape and analyze sentiment
    headlines = scraper.scrape_headlines()
    sentiment = scraper.analyze_sentiment(headlines)
    print(f"News Sentiment: {sentiment:.2f}")

    # 3. Download historical SPY prices
    df = pd.DataFrame(trading.wb.get_bars(config.SPY_SYMBOL, interval="day", count=500))
    df = features.compute_features(df)

    # 4. Train or load model
    try:
        clf = model.load_model()
        print("Loaded existing model.")
    except:
        print("Training new model.")
        model.train_model(df)
        clf = model.load_model()

    # 5. Make prediction
    latest_features = df.iloc[-1][["rsi", "ma_50", "ma_200"]].values
    prediction = model.predict(clf, latest_features)

    # 6. Decide based on sentiment + technicals
    if prediction == 1 and sentiment > 0:
        print("Signal: BUY CALL option")
        option = trading.find_spy_option()
        if option:
            trading.place_order(option_id=option['tickerId'], action="BUY")
    elif prediction == 0 and sentiment < 0:
        print("Signal: BUY PUT option")
        option = trading.find_spy_option()
        if option:
            trading.place_order(option_id=option['tickerId'], action="BUY")
    else:
        print("No clear trade signal today.")

if __name__ == "__main__":
    run()
