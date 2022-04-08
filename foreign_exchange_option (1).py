#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


### foreign Exchange Option ###


# In[6]:


import math

def fx_option_d1(strike, term, spot, volatility, domestic_rate, foreign_rate):
    """Calculate the d1 statistic for Garman Kohlhagen formula for fx option
        >>> '%.10f' % fx_option_d1(152, 91/365, 150, 0.13, 0.03, 0.04)
        '-0.2100058012'
    """
    
    d1 =(math.log(spot/strike) + (domestic_rate - foreign_rate + (volatility*volatility)/2)* term)/(volatility*math.sqrt(term))
    return d1
    


# In[7]:


import math

def fx_option_d2(term, volatility, d1):

    """Calculate the d2 statistic for Garman Kolhagen formula for fx option
        >>> '%.10f' % fx_option_d2(91/365, 0.13, -0.21000580120118273)
        '-0.2749166990'
    """
    
    d2 = d1 - volatility*math.sqrt(term)
    
    return d2


# In[ ]:





# In[8]:


def discount(rate,term):
    """Calculate the discount factor for given simple interest rate and term.
    present_value = future_value * discount(rate, term)
    >>> discount(0.123, 0.0)
    1.0
    >>> discount(0.03, 2.1)
    0.9389434736891332
    """
    # 𝑒−𝑟𝑇

    discount_rate = math.exp((-rate) * term) 
    return discount_rate
    


# In[9]:


from datetime import date 

def years_apart(date1, date2):
    
    """
    Returns the fractional difference in years between the given dates.
    Assumes a 365-day year for the fractional part.
    >>> years_apart(date(1959, 5, 3), date(1960, 5, 3))
    1.0
    >>> years_apart(date(2004, 1, 1), date(2005, 1, 2)) # 365 days even if a leap year
    1.0027397260273974
    >>> years_apart(date(1959, 5, 1), date(2019, 6, 2))
    60.087671232876716
    >>> years_apart(date(2019, 7, 1), date(2019, 4, 1)) # reversed is ok
    0.2493150684931507
    """
   
    if date2 < date1:
        date1,date2 = date2,date1
        
        
    current_date = date1
    count = 0
    
    while current_date < date2:
        current_date = date(current_date.year +1, current_date.month, current_date.day)
        count += 1
        print(current_date)
        
    if current_date == date2:
        fraction = float(count)
        
    else:
        
        current_date = date(current_date.year -1, current_date.month, current_date.day)
        count -=1


        diff = (date2 - current_date).days

        fraction = ((count * 365) + diff)/ 365
    return fraction


# In[10]:


years_apart(date(2019, 7, 1), date(2019, 4, 1))


# In[11]:


def fx_option_price(call, strike, expiration, spot_date,
                    spot, volatility, domestic_rate, foreign_rate):
    """
    Calculates the fair price of a currency option.
    :param call:          True if this is a call option, False if this is a put option
    :param strike:        units of domestic currency per unit of foreign currency to be exchanged
    :param expiration:    date on which the exchange would take place if exercised
    :param spot_date:     date of valuation
    :param spot:          market exchange rate for fx exchanged on spot_date (same units as strike)
    :param volatility:    standard deviation of the logarithmic returns of holding this foreign currency (annualized)
    :param domestic_rate: simple risk-free interest rate from spot_date to expiration_date (annualized)
    :param foreign_rate:  simple risk-free interest rate from spot_date to expiration_date (annualized)
    :return:              option value in domestic currency for one unit of foreign currency

    >>> '%.10f' % fx_option_price(True, 152, date(2019,7,1), date(2019,4,1), 150, 0.13, 0.03, 0.04)
    '2.8110445343'
    >>> '%.10f' % fx_option_price(False, 152, date(2019,7,1), date(2019,4,1), 150, 0.13, 0.03, 0.04)
    '5.1668650332'
    """
    
    term = years_apart(date1=spot_date, date2=expiration)
    discount_rate_foreign = discount(foreign_rate, term)
    discount_rate_domestic = discount(domestic_rate,term)
    d1 = fx_option_d1(strike, term, spot, volatility, domestic_rate, foreign_rate)
    d2 = fx_option_d2(term, volatility, d1)
   
    
    if call == True: # call option
        value = spot * discount_rate_foreign * norm.cdf(d1) - strike * discount_rate_domestic * norm.cdf(d2)
        return '%.10f'% value
    else: # put option
        value = strike * discount_rate_domestic * norm.cdf(- d2) - spot * discount_rate_foreign * norm.cdf(- d1)
        return '%.10f'% value

fx_option_price(True, 152, date(2019,7,1), date(2019,4,1), 150, 0.13, 0.03, 0.04)


# In[ ]:





# In[ ]:




