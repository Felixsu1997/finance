import yfinance as yf

# -----
etf_symbols = ['0056.TW', '00878.TW', '00713.TW']

# -----
etfs = {}
for symbol in etf_symbols:
    etf_data = yf.Ticker(symbol)
    current_price = etf_data.history(period='1d')['Close'][0]  # 獲取最近一日的收盤價
    dividend = 0.51 if symbol == '0056.TW' else 0.27 if symbol == '00878.TW' else 0.68
    etfs[symbol] = {'price': current_price, 'dividend': dividend}

# -----
capital = int(input("請輸入您的總資金（元）："))

# -----
total_ratio = sum(data['dividend'] / data['price'] for data in etfs.values())

# -----
allocation_ratio = {}
for etf, data in etfs.items():
    allocation_ratio[etf] = (data['dividend'] / data['price']) / total_ratio

# -----
total_dividend = 0
for etf, ratio in allocation_ratio.items():
    allocated_capital = capital * ratio  # 分配的資金
    shares = int(allocated_capital // etfs[etf]['price'])  # 每支股票可以買的股數
    dividend = shares * etfs[etf]['dividend'] * 4  # 計算每年總股利收益（每季股利*4）
    total_dividend += dividend  # 累計總現金股利
    print(f"{etf}: 分配資金 {allocated_capital:.2f} 元，購買 {shares} 股，每年預期股利為 {dividend:.2f} 元")

# -----
monthly_dividend = total_dividend / 12
print(f"總年股利收益：{total_dividend:.2f} 元")
print(f"每月預期股利收益：{monthly_dividend:.2f} 元")

# 防止視窗自動關閉
input("按下任意鍵退出...")
