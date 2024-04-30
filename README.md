# Calculate your OKX Transaction Metrics

Metrics supported:
ROI, Win Rate, MDD(maximum drawdown), Profit Factor, Sharpe Ratio

## How to execute

Turn on your local server:

```
pip install -r requirments.txt
python main.py
```

API to calculate metrics:
POST http://localhost:5000/api/v1/metrics

request is your OKX transaction json
response format example:

```json
{
  "message": "Calculation successful",
  "results": {
    "maxDrawdown": "-73.59%",
    "oddsRatio": "0.33",
    "profitFactor": "1.55",
    "roi": "14.83%",
    "sharpeRatio": "-0.24",
    "winRate": "25.00%"
  }
}
```
