from django.conf import settings
import json

import yfinance as yf
from home.models import auto_Ticker


ticker_list = ["ADBE","NFLX","STOR"]
def schedule_api(): 
    print("working")
    for item in ticker_list:
        print(item)
        ticker_name = item
        msft = yf.Ticker(ticker_name)
        enterpriseValue = msft.info['enterpriseValue']
        market_Cap = msft.info['marketCap']
        profitMargins = msft.info['profitMargins']
        fiftyTwoWeekHigh = msft.info['fiftyTwoWeekHigh']
        totalRevenue = msft.info['totalRevenue']
        averageVolume10days = msft.info['averageVolume10days']
        floatShares = msft.info['floatShares']
        heldPercentInsiders = msft.info['heldPercentInsiders']
        heldPercentInstitutions = msft.info['heldPercentInstitutions']
        shortPercentOfFloat = msft.info['shortPercentOfFloat']
        totalCashPerShare = msft.info['totalCashPerShare']
        totalCash = msft.info['totalCash']
        totalDebt = msft.info['totalDebt']
        book_Value = msft.info['bookValue']
        # cashValue = msft.info['bookValue']
        operatingCashflow = msft.info['operatingCashflow']
        Outstanding_Shares = msft.info['sharesOutstanding']
        
        data_entry = auto_Ticker(ticker_name=ticker_name,enterpriseValue=enterpriseValue,market_Cap=market_Cap,profitMargins=profitMargins,fiftyTwoWeekHigh=fiftyTwoWeekHigh,totalRevenue=totalRevenue,averageVolume10days=averageVolume10days,floatShares=floatShares,heldPercentInstitutions=heldPercentInstitutions,heldPercentInsiders=heldPercentInsiders,shortPercentOfFloat=shortPercentOfFloat,totalCashPerShare=totalCashPerShare,totalCash=totalCash,totalDebt=totalDebt,book_Value=book_Value,operatingCashflow=operatingCashflow,Outstanding_Shares=Outstanding_Shares)
        data_entry.save()