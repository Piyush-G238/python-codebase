import pandas
# from datetime import date

complete_data = pandas.read_csv('expense_data.csv')

date_col = complete_data['Date'].to_list()
# convert date columns properly
date_data = []
for eachdate in date_col:
    if eachdate != "":    
        formatted_date = pandas.to_datetime(eachdate).date()
        date_data.append(formatted_date)
# print(date_data)

# total expense for the month
total_exepnse  = complete_data['Amount'].sum()
print(f"total expense as per data: {total_exepnse}")

# expenses by category
grouped_data = complete_data.groupby('Category')
# print(grouped_data.aggregate('sum'))
# grouped_data.aggregate('sum').to_csv('expense_summary.csv')

# daily average
daily_avg = complete_data.groupby('Date').mean()
print(daily_avg)