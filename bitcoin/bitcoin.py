import module as m
import matplotlib.pyplot as plt

url = 'https://www.coingecko.com/price_charts/1/twd/90_days.json'
bitcoin = m.get_price(url)

total = 0
for i in range(0, 2000, 100):
    for j in range(0, 2000, 100):
        tmp_total = m.strategy(bitcoin, 1000000, i, j)
        if tmp_total > total:
            total = tmp_total
            best_ma = i
            best_stop_earn = j 

for i in range(best_ma-100, best_ma+100, 10):
    for j in range(best_stop_earn-100, best_stop_earn+100, 10):
        tmp_total = m.strategy(bitcoin, 1000000, i, j)
        if tmp_total > total:
            total = tmp_total
            best_ma = i
            best_stop_earn = j

print("total=", total, " Best MA=", best_ma, " Best stop earn", best_stop_earn)
bitcoin['ma'] = bitcoin['twd'].rolling(window=best_ma).mean()
bitcoin[['twd', 'ma']].plot(
    kind='line', figsize=[15, 5], xlim=('2021-01-15', '2021-02-28'))
plt.show()
