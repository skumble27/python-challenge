import csv
import statistics
import os

budget_file = ('E:/My Documents/Professional Development/Monash University Data Analytics Boot Camp/GitHubRepo/python-challenge/PyBank/Resources/budget_data.csv')

outputfile = open('E:\My Documents\Professional Development\Monash University Data Analytics Boot Camp\GitHubRepo\python-challenge\PyBank\Analysis\Analysis_PyBank.txt',"w")

##budget_file = os.path.join("Resources", "budget_data.csv")

months = []
profit_loss = []
profit_loss_diff = []
month_list = []
total_months = 0
net_total = 0


with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        months.append(row[0])
        profit_loss.append(row[1])
    
    for month in range(1,len(months)):
        month_list.append(months[month])
        
        
    
    for i, (cur, nxt) in enumerate(zip(profit_loss, profit_loss[1:])):
        changes = float(nxt) - float(cur)
        profit_loss_diff.append(changes)
    
    
## Calculating the Average
average_change = round(statistics.mean(profit_loss_diff), 2)               
## Calculating the maximum increase
max_increase = round(int(max(profit_loss_diff)),0)

## Calculating the maximum decrease
max_decrease = round(int(min(profit_loss_diff)),0)

## Referring to the month where max increase occurred
highest_month = profit_loss_diff.index(max_increase)
top_month = month_list[highest_month]


## Referring to the month where max decrease occurred
lowest_month = profit_loss_diff.index(max_decrease)
bottom_month = month_list[lowest_month]


## Providing an output on the Terminal

print(f' Financial Analysis')
print(f'-------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {top_month} (${max_increase})')
print(f'Greatest Increase in Profits: {bottom_month} (${max_decrease})')

## Writing the outcome of the Code into Text


outputfile.write(f' Financial Analysis\n')
outputfile.write(f'-------------------------------------\n')
outputfile.write(f'Total Months: {total_months}\n')
outputfile.write(f'Total: ${net_total}\n')
outputfile.write(f'Average Change: ${average_change}\n')
outputfile.write(f'Greatest Increase in Profits: {top_month} (${max_increase})\n')
outputfile.write(f'Greatest Increase in Profits: {bottom_month} (${max_decrease})\n')
outputfile.close()
