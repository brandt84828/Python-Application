import requests
from io import StringIO
import pandas as pd
import datetime

def get_setting():
    res = []
    try:
        with open('stock.txt') as f:
            content = f.readlines()
            print("Content : ", content)
            stock, start_date, end_date = content[0].split(',')
            res = [stock, start_date, end_date]
    except Exception as e:
        print("Read stock.txt error.")
    return res

def get_data():
    data = get_setting()
    dates = []
    start_date = datetime.datetime.strptime(data[1], '%Y%m%d')
    end_date = datetime.datetime.strptime(data[2], '%Y%m%d')
    for day in range((end_date - start_date).days + 1):
        date = start_date + datetime.timedelta(days=day)
        if date.weekday() < 6:
            dates.append(date.strftime('%Y%m%d'))
    return data[0], dates

def crawl_data(date, symbol):
    r = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')
    r_text = [i for i in r.text.split('\n') if len(i.split('",')) == 17 and i[0] != '=']
    df = pd.read_csv(StringIO("\n".join(r_text)), header=0)
    df = df.drop(columns=['Unnamed: 16'])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0, "日期", date)
    return list(filter_df.iloc[0]), filter_df.columns
    