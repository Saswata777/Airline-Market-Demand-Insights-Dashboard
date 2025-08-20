import time
import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

def load_trends(kw_list, geo, timeframe):
    """Fetch Google Trends data for keywords and return a DataFrame."""
    batches = [kw_list[i:i+5] for i in range(0, len(kw_list), 5)]
    frames = []
    for batch in batches:
        pytrends.build_payload(batch, cat=0, timeframe=timeframe, geo=geo, gprop='')
        df = pytrends.interest_over_time()
        if df.empty:
            continue
        df = df.drop(columns=['isPartial'], errors='ignore')
        df = df.reset_index().rename(columns={'date': 'date'})
        frames.append(df)
        time.sleep(1.2)
    if not frames:
        return pd.DataFrame()
    out = frames[0]
    for f in frames[1:]:
        out = out.merge(f, on='date', how='outer')
    long_df = out.melt(id_vars=['date'], var_name='keyword', value_name='interest').dropna()
    long_df['route'] = long_df['keyword'].str.replace(' flights', '', regex=False).str.title()
    return long_df.sort_values('date')
