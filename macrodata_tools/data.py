import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt


def get_cpi(start="2000-01-01"):
    """
    Download CPI data from FRED
    """
    cpi = web.DataReader("CPIAUCSL", "fred", start)
    cpi.columns = ["CPI"]
    return cpi


def compute_inflation(cpi):
    """
    Compute year-over-year inflation
    """
    inflation = cpi.pct_change(12) * 100
    inflation.columns = ["Inflation"]
    return inflation


def inflation_summary(inflation):
    """
    Basic statistics of inflation
    """
    return inflation.describe()


def plot_inflation(inflation):
    """
    Plot inflation over time
    """
    inflation.plot(title="US Inflation Rate")
    plt.show()