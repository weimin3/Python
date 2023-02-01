"""
练习： 【[CODE]()】
>
> 定义如下变量：
> - name: apple
> - stock_price: 当前股价
> - stock_code:00100
> - stock_price_daily_growth_factor:每日增长系数，1.2
> - growth_days: 增长天数，7
> 使用字符串格式化输出，小数点精度2位
"""

name = "apple"
stock_price = 19.99
stock_code = "00100"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print("公司：%s , 股票代码： %s , 当前股价： %.2f, 每日增长系数是：%.1f, 经过 %s 天增长后，股价达到了：%.2f " %(name, stock_code,stock_price,stock_price_daily_growth_factor,growth_days,(stock_price * (stock_price_daily_growth_factor ** growth_days))))
print(f"公司：{name}, 股票代码：{stock_code} , 当前股价：{stock_price}, 每日增长系数是：{stock_price_daily_growth_factor}, 经过 {growth_days} 天增长后，股价达到了：{(stock_price * (stock_price_daily_growth_factor ** growth_days))} " )

