import numpy as np

def straddle(prices, strike, call_premium, put_premium):
    
    call = np.maximum(prices - strike, 0) - call_premium
    put = np.maximum(strike - prices, 0) - put_premium
    return call + put

def strangle(prices, call_strike, call_premium, put_strike, put_premium):
    
    call = np.maximum(prices - call_strike, 0) - call_premium
    put = np.maximum(put_strike - prices, 0) - put_premium
    return call + put

def bull_call_spread(prices, long_strike, long_premium, short_strike, short_premium):
    
    long_call = np.maximum(prices - long_strike, 0) - long_premium
    short_call = -1 * (np.maximum(prices - short_strike, 0) - short_premium)
    return long_call + short_call

def bear_put_spread(prices, long_strike, long_premium, short_strike, short_premium):
    
    long_put = np.maximum(long_strike - prices, 0) - long_premium
    short_put = -1 * (np.maximum(short_strike - prices, 0) - short_premium)
    return long_put + short_put

def iron_condor(prices, lower_put_strike, lower_put_premium,
                higher_put_strike, higher_put_premium,
                lower_call_strike, lower_call_premium,
                higher_call_strike, higher_call_premium):
    
    long_put = np.maximum(lower_put_strike - prices, 0) - lower_put_premium
    short_put = -1 * (np.maximum(higher_put_strike - prices, 0) - higher_put_premium)
    short_call = -1 * (np.maximum(prices - lower_call_strike, 0) - lower_call_premium)
    long_call = np.maximum(prices - higher_call_strike, 0) - higher_call_premium
    return long_put + short_put + short_call + long_call
