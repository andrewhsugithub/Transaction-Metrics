# def test(data):
#     for transaction in data:
#         if float(transaction['fillPnl']) !=0 and transaction['side']=="buy":
#             print(transaction)

# https://crypto.com/university/how-to-calculate-roi-for-crypto#:~:text=Calculating%20ROI%20for%20crypto%20assets,value%2C%20and%20multiplying%20by%20100.
def roi(data, initial_investment=8000):
    total_profit = 0.0
    
    for transaction in data:
        if float(transaction['fillPnl'])==0: continue
        total_profit += float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee'])
        
    return f'{total_profit/initial_investment*100:.2f}%'

# https://www.sightfull.com/glossary/opportunity-win-rate/
def win_rate(data):
    wins = 0
    losses = 0
    
    for transaction in data:
        if float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee']) > 0:
            wins += 1
        elif float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee']) < 0:
            losses += 1
            
    return f'{wins/(wins+losses)*100:.2f}%'

# https://www.investopedia.com/terms/w/win-loss-ratio.asp
def odds_ratio(data):
    wins = 0
    losses = 0
    
    for transaction in data:
        if float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee']) > 0:
            wins += 1
        elif float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee']) < 0:
            losses += 1
            
    return f'{wins/losses:.2f}'

# https://www.stockfeel.com.tw/%E6%9C%80%E5%A4%A7%E5%9B%9E%E6%92%A4-max-drawdown-%E7%AD%96%E7%95%A5%E7%AE%A1%E7%90%86/
# https://www.investopedia.com/terms/m/maximum-drawdown-mdd.asp
def max_drawdown(data):
    cumulative_profit = 0.0
    peak = -float('inf')
    max_drawdown = float('inf')
    
    for transaction in data:
        if float(transaction['fillPnl'])==0: continue
        cumulative_profit += float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee'])
        peak = max(peak, cumulative_profit)
        max_drawdown = min(max_drawdown, (cumulative_profit-peak)/peak*100)
        
    return f'{max_drawdown:.2f}%'

# https://www.instatrade.com/blog/16-profit-factor#:~:text=The%20profit%20factor%20is%20calculated,earned%20two%20dollars%20in%20profit.
def profit_factor(data):
    total_profit = 0.0
    total_loss = 0.0
    
    for transaction in data:
        if float(transaction['fillPnl']) > 0:
            total_profit += float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee'])
        elif float(transaction['fillPnl']) < 0:
            total_loss += float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee'])
            
    return f'{total_profit/abs(total_loss):.2f}'

# https://gocardless.com/guides/posts/sharpe-ratio/
def sharpe_ratio(data, initial_investment=8000):
    risk_free_rate = 1.21  # January 31st 2024 https://tradingeconomics.com/taiwan/government-bond-yield
    prev = initial_investment
    total_return = 0.0
    total_transactions = 0
    
    # calculate average return
    for transaction in data:
        if float(transaction['fillPnl'])==0: continue
        total_transactions += 1
        curr = prev + float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee'])
        total_return += (curr-prev)/prev*100
        prev = curr
    avg_return = total_return/total_transactions
    
    # calculate excess return
    excess_return = avg_return - risk_free_rate
    
    # calculate standard deviation
    std_return = 0.0
    for transaction in data:
        if float(transaction['fillPnl'])==0: continue
        curr = prev + float(transaction['fillPnl'])*float(transaction['fillSz']) + float(transaction['fee'])
        std_return += (((curr-prev)/prev*100-avg_return)**2)/total_transactions
        prev = curr
        
    std_return = (std_return)**0.5
    
    return f'{excess_return/std_return:.2f}'

def main(data, initial_investment=8000):
    return {
        "roi": roi(data, initial_investment),
        "winRate": win_rate(data),
        "maxDrawdown":  max_drawdown(data),
        "oddsRatio": odds_ratio(data),
        "profitFactor": profit_factor(data),
        "sharpeRatio": sharpe_ratio(data, initial_investment)
    }