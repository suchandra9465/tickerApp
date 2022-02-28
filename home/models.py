from django.db import models

# Create your models here.
class Info(models.Model):
    ticker_name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    sector = models.CharField(max_length=50)
    biotech_Speciality = models.CharField(max_length=50)
    biotech_Data = models.CharField(max_length=50)
    regulatory = models.CharField(max_length=50)
    other = models.CharField(max_length=50)
    catalyst_Expectation = models.CharField(max_length=50)
    catalyst_Outcome = models.CharField(max_length=50)
    activeshelf_ATM = models.CharField(max_length=50)
    catalyst_Timing = models.CharField(max_length=50)
    catalyst_PR = models.CharField(max_length=50)
    pre_Catalyst_1m_RU_RD = models.CharField(max_length=50)
    Pre_Catalyst_1m_RU_RD_Pattern = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    volume_dollar = models.CharField(max_length=50)
    catalyst_1d_move_percent = models.CharField(max_length=50)    
    option_percent_Anticipated_Move = models.CharField(max_length=50)
    catalyst_intraday_moves_percent = models.CharField(max_length=50)
    post_Catalyst_1d_RU_RD = models.CharField(max_length=50)
    post_Catalyst_1w_RU_RD = models.CharField(max_length=50)
    post_Catalyst_2w_RU_RD = models.CharField(max_length=50)
    post_Catalyst_3w_RU_RD = models.CharField(max_length=50)
    market_Cap = models.CharField(max_length=50)
    enterprise_Value = models.CharField(max_length=50)
    book_Value = models.CharField(max_length=50)
    heldPercentInstitutions = models.CharField(max_length=50)
    heldPercentInsiders = models.CharField(max_length=50)
    shortPercentOfFloat = models.CharField(max_length=50)
    Outstanding_Shares = models.CharField(max_length=50)
    floatShares = models.CharField(max_length=50)
    totalCash = models.CharField(max_length=50)
    totalDebt = models.CharField(max_length=50)
    operatingCashflow = models.CharField(max_length=50)
    profitMargins = models.CharField(max_length=50)
    fiftyTwoWeekHigh = models.CharField(max_length=50)
    totalRevenue = models.CharField(max_length=50)
    averageVolume10days = models.CharField(max_length=50)
    
    totalCashPerShare = models.CharField(max_length=50)
    technicalIndicators = models.TextField() 
    
    
    
    
    
    # shortPercentOfFloat = models.CharField(max_length=50)