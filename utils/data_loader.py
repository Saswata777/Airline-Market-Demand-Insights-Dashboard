# import time
# import pandas as pd
# from pytrends.request import TrendReq

# pytrends = TrendReq(hl='en-US', tz=360)

# def load_trends(kw_list, geo, timeframe):
#     """Fetch Google Trends data for keywords and return a DataFrame."""
#     batches = [kw_list[i:i+5] for i in range(0, len(kw_list), 5)]
#     frames = []
#     for batch in batches:
#         pytrends.build_payload(batch, cat=0, timeframe=timeframe, geo=geo, gprop='')
#         df = pytrends.interest_over_time()
#         if df.empty:
#             continue
#         df = df.drop(columns=['isPartial'], errors='ignore')
#         df = df.reset_index().rename(columns={'date': 'date'})
#         frames.append(df)
#         time.sleep(1.2)
#     if not frames:
#         return pd.DataFrame()
#     out = frames[0]
#     for f in frames[1:]:
#         out = out.merge(f, on='date', how='outer')
#     long_df = out.melt(id_vars=['date'], var_name='keyword', value_name='interest').dropna()
#     long_df['route'] = long_df['keyword'].str.replace(' flights', '', regex=False).str.title()
#     return long_df.sort_values('date')
import time
import random
import pandas as pd
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def load_trends(kw_list, geo, timeframe, max_retries=3, min_delay=5, max_delay=10):
    """Fetch Google Trends data for keywords and return a DataFrame."""
    pytrends = TrendReq(hl='en-US', tz=360)
    
    # Break into batches of 5 keywords max
    batches = [kw_list[i:i+5] for i in range(0, len(kw_list), 5)]
    frames = []

    for batch in batches:
        retries = 0
        while retries < max_retries:
            try:
                pytrends.build_payload(batch, cat=0, timeframe=timeframe, geo=geo, gprop='')
                df = pytrends.interest_over_time()
                if df.empty:
                    break  # skip empty batch
                df = df.drop(columns=['isPartial'], errors='ignore')
                df = df.reset_index().rename(columns={'date': 'date'})
                frames.append(df)
                # Randomized sleep to avoid being flagged
                time.sleep(random.uniform(min_delay, max_delay))
                break  # success, move to next batch
            except TooManyRequestsError:
                retries += 1
                wait_time = 60 * retries  # exponential backoff: 60s, 120s, ...
                print(f"Rate limit hit. Retrying in {wait_time}s (attempt {retries}/{max_retries})...")
                time.sleep(wait_time)
        else:
            print(f"Failed to fetch data for batch: {batch}")

    # If no data collected, return empty DataFrame
    if not frames:
        return pd.DataFrame()

    # Merge all batches
    out = frames[0]
    for f in frames[1:]:
        out = out.merge(f, on='date', how='outer')

    # Convert to long format
    long_df = out.melt(id_vars=['date'], var_name='keyword', value_name='interest').dropna()
    long_df['route'] = long_df['keyword'].str.replace(' flights', '', regex=False).str.title()

    return long_df.sort_values('date')
