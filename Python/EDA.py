import pandas as pd
import matplotlib.pyplot as plt
----------------------------------------------
daily_sales = pd.read_csv("file_path")
weekly_sales = pd.read_csv("file_path")
monthly_sales = pd.read_csv("file_path")
----------------------------------------------
daily_sales_info = daily_sales.info(), daily_sales.head()
weekly_sales_info = weekly_sales.info(), weekly_sales.head()
monthly_sales_info = monthly_sales.info(), monthly_sales.head()

daily_sales_info, weekly_sales_info, monthly_sales_info
----------------------------------------------
daily_sales['datum'] = pd.to_datetime(daily_sales['datum'])
weekly_sales['datum'] = pd.to_datetime(weekly_sales['datum'])
monthly_sales['datum'] = pd.to_datetime(monthly_sales['datum'])
----------------------------------------------
numeric_columns = daily_sales.iloc[:, 1:].select_dtypes(include=['float', 'int']).columns
daily_sales['Total Daily Sales'] = daily_sales[numeric_columns].sum(axis=1)

weekly_sales['Total Weekly Sales'] = weekly_sales.iloc[:, 1:].sum(axis=1)

monthly_sales['Total Monthly Sales'] = monthly_sales.iloc[:, 1:].sum(axis=1)

monthly_sales['Monthly Growth'] = monthly_sales['Total Monthly Sales'].pct_change()

daily_sales['Cumulative Daily Sales'] = daily_sales['Total Daily Sales'].cumsum()
monthly_sales['Cumulative Monthly Sales'] = monthly_sales['Total Monthly Sales'].cumsum()

daily_summary = daily_sales[['datum', 'Total Daily Sales', 'Cumulative Daily Sales']].tail()
weekly_summary = weekly_sales[['datum', 'Total Weekly Sales']].tail()
monthly_summary = monthly_sales[['datum', 'Total Monthly Sales', 'Monthly Growth', 'Cumulative Monthly Sales']].tail()

daily_summary, weekly_summary, monthly_summary
----------------------------------------------