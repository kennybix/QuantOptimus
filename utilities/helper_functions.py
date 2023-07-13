import requests
import time





def fetch_binance_historical_data(symbol, interval, start_time, end_time):
    """
    Fetches historical k-line data from Binance API for a given symbol, interval, start time, and end time.
    
    :param symbol: str, trading pair symbol (e.g., 'BTCUSDT' for Bitcoin/USDT)
    :param interval: str, timeframe for the historical data (e.g., '1d' for daily)
    :param start_time: int, start timestamp in milliseconds
    :param end_time: int, end timestamp in milliseconds
    :return: list of dictionaries, historical k-line data
    """
    # Define API endpoint
    endpoint = 'https://api.binance.com/api/v3/klines'
    
    # Initialize empty list to store historical data
    historical_data = []
    
    # Loop until end time is reached
    while start_time < end_time:
        # Calculate remaining time until end time or maximum allowed timeframe (500 data points)

        if interval[-1] == 'h':
            interval_size = (int(interval[0]) * 60) - 1
        else:
            interval_size = int(interval[:-1])
        
        remaining_time = min(end_time - start_time, 500 * interval_size * 60 * 1000)
        
        # Define API parameters for current request
        params = {
            'symbol': symbol,
            'interval': interval,
            'startTime': start_time,
            'endTime': start_time + remaining_time,
            'limit': 500,
        }
        
        # Send API request and parse response
        response = requests.get(endpoint, params=params)
        data = response.json()

        # display(len(data)) 
        
        # Append fetched data to historical_data list
        historical_data.extend(data)
        
        # Update start time for next request
        start_time += remaining_time + (int(interval[:-1]) * 60 * 1000)
        
        # Add delay to avoid hitting API rate limits (optional)
        time.sleep(1)
    
    return historical_data
