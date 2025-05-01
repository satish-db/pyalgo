from openbb import obb
from utils import cumulative_compound_returns, cumulative_simple_returns, returns, rolling_volatility_look_back, volatility_annualized

obb.user.preferences.output_type = "dataframe"

def main():
    print("Hello from pyalgo!")


def calculate_returns():
    data = obb.equity.price.historical("AAPL",provider="yfinance")
    print(data.head())
    returns_df=returns(data)
    print(returns_df.head(20))
    print(volatility_annualized(data))
    print(rolling_volatility_look_back(data,25))
    print(cumulative_simple_returns(data))
    print(cumulative_compound_returns(data))








if __name__ == "__main__":
    
    calculate_returns()
