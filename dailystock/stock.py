import matplotlib.pyplot as plt
import crawler
import time
import pandas as pd

all_list = []
stock_symbol, dates = crawler.get_data()
for date in dates:
    time.sleep(1)
    try:
        data = crawler.crawl_data(date, stock_symbol)
        all_list.append(data[0])
        df_columns = data[1]
        print(" OK! date = " + date + ", stock_symbol = " + stock_symbol) 
    except:
        print("Error! date = " + date + ", stock_symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)

day = all_df["日期"].astype(str)
open_price = all_df["開盤價"].str.replace(',', '').astype(float)
close_price = all_df["收盤價"].str.replace(',', '').astype(float)
high_price = all_df["最高價"].str.replace(',', '').astype(float)
low_price = all_df["最低價"].str.replace(',', '').astype(float)
volumes = all_df["成交股數"].str.replace(',', '').astype(float)

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 15), dpi=100)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
ax.set_title(stock_symbol+"  開盤價、收盤價 ( " + dates[0] + " ~ " + dates[-1] + " )")

ax.plot(day, open_price, 's-', color='r', label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close_price, 'o-', color='b', label="Close Price")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])

# step 4 show plot
plt.show()