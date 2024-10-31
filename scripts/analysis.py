import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error


# data_loading

def load_data(file_path):
    """
    Load Brent oil prices data from a CSV file and convert the date column to datetime.
    
    Parameters:
        file_path (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded dataset with the 'Date' column as datetime.
    """
    data = pd.read_csv(file_path)
    
    # Parse the 'Date' column with the specified format
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%b-%y', errors='coerce')
    
    # Drop rows with unparseable dates if any
    data = data.dropna(subset=['Date'])
    
    data.set_index('Date', inplace=True)
    return data



def preprocess_data(data):
    """
    Handle missing values and perform basic preprocessing.
    
    Parameters:
        data (pd.DataFrame): Loaded dataset with 'Price' column.
        
    Returns:
        pd.DataFrame: Preprocessed dataset.
    """
    # Check for missing values in 'Price' and fill with interpolation
    if data['Price'].isnull().sum() > 0:
        data['Price'].interpolate(method='linear', inplace=True)
    
    # Remove any remaining NA values
    data.dropna(inplace=True)
    
    return data



def plot_price(data):
    """
    Plot the Brent oil prices over time.
    
    Parameters:
        data (pd.DataFrame): Dataset with 'Price' column.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Price'], label='Brent Oil Price')
    plt.title('Brent Oil Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

def rolling_statistics(data, window=30):
    """
    Calculate and plot rolling mean and standard deviation.
    
    Parameters:
        data (pd.DataFrame): Dataset with 'Price' column.
        window (int): Window size for rolling calculations.
    """
    rolling_mean = data['Price'].rolling(window=window).mean()
    rolling_std = data['Price'].rolling(window=window).std()
    
    plt.figure(figsize=(12, 6))
    plt.plot(data['Price'], label='Original')
    plt.plot(rolling_mean, color='orange', label=f'{window}-Day Rolling Mean')
    plt.plot(rolling_std, color='green', label=f'{window}-Day Rolling Std')
    plt.title('Rolling Mean & Standard Deviation')
    plt.legend()
    plt.show()


# feature_engineering

def add_moving_averages(data, windows=[7, 30, 365]):
    """
    Add moving average features to the data for specified windows.
    
    Parameters:
        data (pd.DataFrame): Dataset with 'Price' column.
        windows (list of int): List of window sizes for moving averages.
        
    Returns:
        pd.DataFrame: Dataset with moving average columns added.
    """
    for window in windows:
        data[f'MA_{window}'] = data['Price'].rolling(window=window).mean()
    return data


# model_training

def train_arima_model(data, order=(5, 1, 0)):
    """
    Train an ARIMA model on the data.
    
    Parameters:
        data (pd.DataFrame): Dataset with 'Price' column.
        order (tuple): Order for the ARIMA model.
        
    Returns:
        ARIMA: Fitted ARIMA model.
    """
    model = ARIMA(data['Price'], order=order)
    model_fit = model.fit()
    return model_fit

# evaluation

def evaluate_model(model_fit, data, steps=30):
    """
    Evaluate the model by forecasting and calculating error metrics.
    
    Parameters:
        model_fit (ARIMA): Fitted ARIMA model.
        data (pd.DataFrame): Original dataset with 'Price' column.
        steps (int): Number of steps to forecast.
        
    Returns:
        None
    """
    forecast = model_fit.forecast(steps=steps)
    forecast_index = pd.date_range(data.index[-1], periods=steps + 1, freq='D')[1:]
    
    plt.figure(figsize=(12, 6))
    plt.plot(data['Price'], label='Actual')
    plt.plot(forecast_index, forecast, label='Forecast', color='red')
    plt.title('Price Forecast')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
    
    mae = mean_absolute_error(data['Price'][-steps:], forecast)
    rmse = np.sqrt(mean_squared_error(data['Price'][-steps:], forecast))
    
    print(f'Mean Absolute Error (MAE): {mae}')
    print(f'Root Mean Squared Error (RMSE): {rmse}')
