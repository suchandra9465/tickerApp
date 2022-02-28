from django.shortcuts import render,redirect

# from django.utils import timezone
import yfinance as yf
from .models import Info

# Create your views here.
def form_method(request):
    # context = {}
    if request.method == 'POST':
        ticker_name = request.POST.get('ticker_name')
        date = request.POST.get('date')
        country = request.POST.get('country')
        print(ticker_name,date)
        msft = yf.Ticker(ticker_name)
        print(msft.info['enterpriseValue'])
        
        sector = request.POST.get('sector')
        biotech_speciality = request.POST.get('biotech_speciality')
        biotech_data = request.POST.get('biotech_data')
        regulatory = request.POST.get('regulatory')
        others = request.POST.get('others')
        catalyst_expectation = request.POST.get('catalyst_expectation')
        catalyst_outcome = request.POST.get('catalyst_outcome')
        activeshelf_ATM = request.POST.get('activeshelf_ATM')
        catalyst_timing = request.POST.get('catalyst_timing')
        catalyst_PR = request.POST.get('catalyst_PR')
        pre_Catalyst_1m_RU_RD = request.POST.get('pre_Catalyst_1m_RU_RD')
        Pre_Catalyst_1m_RU_RD_Pattern = request.POST.get('Pre_Catalyst_1m_RU_RD_Pattern')
        enterpriseValue = msft.info['enterpriseValue']
        marketCap = msft.info['marketCap']
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
        bookValue = msft.info['bookValue']
        # cashValue = msft.info['bookValue']
        operatingCashflow = msft.info['operatingCashflow']
        sharesOutstanding = msft.info['sharesOutstanding']
        volume = request.POST.get('volume')
        volume_dollar = request.POST.get('volume_dollar')
        catalyst_1d_move_percent = request.POST.get('catalyst_1d_move_percent')
        # volume_dollar = msft.info['volume_dollar']
        option_percent_Anticipated_Move = request.POST.get('option_percent_Anticipated_Move')
        catalyst_intraday_moves_percent = request.POST.get('catalyst_intraday_moves_percent')
        post_Catalyst_1d_RU_RD = request.POST.get('post_Catalyst_1d_RU_RD')
        post_Catalyst_1w_RU_RD = request.POST.get('post_Catalyst_1w_RU_RD')
        post_Catalyst_2w_RU_RD = request.POST.get('post_Catalyst_2w_RU_RD')
        post_Catalyst_3w_RU_RD = request.POST.get('post_Catalyst_3w_RU_RD')
        technicalIndicators = request.POST.get('technicalIndicators')
        data_entry = Info(ticker_name=ticker_name,date=date,country=country,sector=sector,biotech_Speciality=biotech_speciality,biotech_Data=biotech_data,regulatory=regulatory,other=others,catalyst_Expectation=catalyst_expectation,catalyst_Outcome=catalyst_outcome,activeshelf_ATM=activeshelf_ATM,catalyst_Timing=catalyst_timing,catalyst_PR=catalyst_PR,pre_Catalyst_1m_RU_RD=pre_Catalyst_1m_RU_RD,Pre_Catalyst_1m_RU_RD_Pattern=Pre_Catalyst_1m_RU_RD_Pattern,enterprise_Value=enterpriseValue,market_Cap=marketCap,profitMargins=profitMargins,fiftyTwoWeekHigh=fiftyTwoWeekHigh,totalRevenue=totalRevenue,averageVolume10days=averageVolume10days,floatShares=floatShares,heldPercentInsiders=heldPercentInsiders,heldPercentInstitutions=heldPercentInstitutions,shortPercentOfFloat=shortPercentOfFloat,totalCashPerShare=totalCashPerShare,totalCash=totalCash,totalDebt=totalDebt,book_Value=bookValue,operatingCashflow=operatingCashflow,Outstanding_Shares=sharesOutstanding,volume=volume,volume_dollar=volume_dollar,catalyst_1d_move_percent=catalyst_1d_move_percent,option_percent_Anticipated_Move=option_percent_Anticipated_Move,catalyst_intraday_moves_percent=catalyst_intraday_moves_percent,post_Catalyst_1d_RU_RD=post_Catalyst_1d_RU_RD,post_Catalyst_1w_RU_RD=post_Catalyst_1w_RU_RD,post_Catalyst_2w_RU_RD=post_Catalyst_2w_RU_RD,post_Catalyst_3w_RU_RD=post_Catalyst_3w_RU_RD,technicalIndicators=technicalIndicators)
        data_entry.save()
        
        return redirect('form_method')
    
        
    
    return render(request,'home/dj_home.html')


def dashboard(request):
    context = {}
    form_data = Info.objects.all().order_by('-id')[:5]
    context['form_data'] = form_data
    # if request.method == 'POST':Market Cap, Book Value, Cash Value, 
    # Institutional %, Insider %, Short %, Outstanding Shares, Float, 
    # Cash, Revenue, Debt, Revenue, Profit Margin, Diluted EPS, Option % Anticipated Move				

    # pass   
    # ticker_name = request.session.get('ticker_name')
    # date = request.session.get('date')
    # print(ticker_name,date)
    # msft = yf.Ticker(ticker_name)
    # print(msft.info['enterpriseValue'])
    # context['enterpriseValue'] = msft.info['enterpriseValue']
    # context['marketCap'] = msft.info['marketCap']
    # context['profitMargins'] = msft.info['profitMargins']
    # context['fiftyTwoWeekHigh'] = msft.info['fiftyTwoWeekHigh']
    # context['totalRevenue'] = msft.info['totalRevenue']
    # context['averageVolume10days'] = msft.info['averageVolume10days']
    # context['floatShares'] = msft.info['floatShares']
    # context['heldPercentInsiders'] = msft.info['heldPercentInsiders']
    # context['heldPercentInstitutions'] = msft.info['heldPercentInstitutions']
    # context['shortPercentOfFloat'] = msft.info['shortPercentOfFloat']
    # context['totalCashPerShare'] = msft.info['totalCashPerShare']
    # context['totalCash'] = msft.info['totalCash']
    # context['totalDebt'] = msft.info['totalDebt']
    # context['bookValue'] = msft.info['bookValue']
    # context['operatingCashflow'] = msft.info['operatingCashflow']
    # context['shortPercentOfFloat'] = msft.info['shortPercentOfFloat']
    
    
    
    
        
        
        
    return render(request,'home/dashboard.html',context)