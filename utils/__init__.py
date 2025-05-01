import pandas as pd
import numpy as np

def returns(df:pd.DataFrame,simple_returns_periods=1,compound_shift=1)-> pd.DataFrame:
    """
    Calculate simple and compound returns for a given DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing at least a 'close' column with price data.
    simple_returns_periods (int): Number of periods to use for calculating simple returns. Default is 1.
    compound_shift (int): Number of periods to shift for calculating compound returns. Default is 1.

    Returns:
    pd.DataFrame: DataFrame with additional columns 'simple' and 'compound' for the calculated returns.
    """
    df["simple"]= df["close"].pct_change(periods=simple_returns_periods)
    df['compound'] =  np.log(df["close"]/df["close"].shift(compound_shift))
    return df

def volatility_annualized(df:pd.DataFrame)-> float :
    
    """
    Calculate the annualized volatility of a given DataFrame.
    Parameters:
    df (pd.DataFrame): DataFrame containing at least a 'close' column with price data.
    Returns:
    float: The annualized volatility of the returns based on the 'close' prices.
    """
    close = df["close"]
    returns  = close.pct_change()
    std_dev= returns.dropna().std()
    annualized_std_dev = std_dev * np.sqrt(252)
    return annualized_std_dev

def rolling_volatility_look_back(df:pd.DataFrame,window=22) -> float :
    """
    Calculate the rolling annualized volatility over a specified look-back window.

    Parameters:
    df (pd.DataFrame): DataFrame containing at least a 'close' column with price data.
    window (int): The number of periods to use for the rolling calculation. Default is 22.

    Returns:
    float: The rolling annualized volatility of the returns based on the 'close' prices.
    """
    close = df["close"]
    return close.pct_change().rolling(window=window).std()*np.sqrt(252)

def cumulative_simple_returns(df:pd.DataFrame) -> pd.Series:
    """
    Calculate the cumulative simple returns for a given DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing at least a 'close' column with price data.

    Returns:
    pd.Series: A Series representing the cumulative simple returns of the 'close' prices.
    """
    close = df["close"]
    returns  = close.pct_change()
    #replace nan with 0
    returns[np.isnan(returns)] =0 
    returns +=1
    cumulative_simple_returns = returns.cumprod() - 1
    return cumulative_simple_returns

def cumulative_compound_returns(df:pd.DataFrame) -> pd.Series:
    """
    Calculate the cumulative compound returns for a given DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame containing at least a 'close' column with price data.

    Returns:
    pd.Series: A Series representing the cumulative compound returns of the 'close' prices.
    """
    close = df["close"]
    log_returns = np.log(close/close.shift())
    cumulative_log_returns = log_returns.cumsum()
    return cumulative_log_returns



