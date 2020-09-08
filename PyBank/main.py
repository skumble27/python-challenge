import os
import csv
import statistics

budget_file = os.path.join("Resources", "budget_data.csv")
output_budget_file = os.path.join("Analysis", 'Analysis_PyBank.txt', 'w')

months = []
months_list_indexing = []
profit_loss = []
total_months = 0
profit_loss_diff_list = []
total_profit_loss = 0

with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    csvheader = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        total_profit_loss += int(row[1])
        total_months += 1
        profit_loss.append(row[1])
        

    ## This new list will be required when we want to find the month        that had the highest and lowest profit-loss change
    
    for month in range(1,len(months)):
        months_list_indexing.append(months[month])

    ## In this code, the difference of values from the current and          previous months will be calcuated and appended to a new list

    for i, (pastmnth, presmnth) in enumerate(zip(profit_loss, profit_loss[1:])):
        changes = float(presmnth) - float(pastmnth)
        profit_loss_diff_list.append(changes)

## Calculating the average change in profit and loss
average_change = statistics.mean(profit_loss_diff_list)

maximum_increase_profit = max(profit_loss_diff_list)
maximum_decrease_profit = min(profit_loss_diff_list)

month_max = profit_loss_diff_list.index(maximum_increase_profit)
month_max = months_list_indexing[month_max]

month_min = profit_loss_diff_list.index(maximum_decrease_profit)
month_min = months_list_indexing[month_min]


## Providing an output to the terminal
print(f' Financial Analysis')
print(f'-------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {month_max} (${maximum_increase_profit})')
print(f'Greatest Increase in Profits: {month_min} (${maximum_decrease_profit})')
   
