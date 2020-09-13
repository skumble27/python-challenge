## PyBank Challenge
## Importing relevant modules for analyses
import os
import csv
import statistics

## File path to access the CSV data
py_bank_file = os.path.join("Resources", "budget_data.csv")

## File path to export the data into a text format
py_bank_outputfile = os.path.join("Analysis","Analysis_PyBank.txt")

## Declaring the variables to calculate profit/loss changes
months = []
months_indexing = []
profit_loss_total = 0
total_months = 0
profit_loss_change = []
profit_loss_list = []

## Opening and Reading the CSV File
with open(py_bank_file) as csvfile:

    ## Create a variable to read the CSV File
    csvreader = csv.reader(csvfile, delimiter=',')

    ## Read the header in the document
    csvheader = next(csvreader)

    ## Looping through the rows to obtain the relevant data
    for row in csvreader:
        
        ## Adding the total number of months
        total_months +=1
        
        ## Summing the total profit/loss 
        profit_loss_total += int(row[1])
        
        ## Adding the months column to a new list
        months.append(row[0])
        
        ## Adding the profit/loss column to a new list
        profit_loss_list.append(row[1])

        

    # Profit/loss changes are determined at the end of the month. In this instance,
    # the profit/loss statements commence in Jan-2010 and therefore, the difference
    # will be calculated in the month of february. In order to allow for correct indexing,
    # a new list will be created that tallies the months starting from feb-2010
    
    for month in range(1,len(months)):
        months_indexing.append(months[month])
    
    # A new list will be created that lists the profit/loss difference
    # for each month
    for i, (pastmnth, presmnth) in enumerate(zip(profit_loss_list, profit_loss_list[1:])):
        changes = int(presmnth) - int(pastmnth)
        profit_loss_change.append(changes)

## Calculating the average profit loss change
average_change = statistics.mean(profit_loss_change)

## Calculating maximum increase and decrease in profit/loss
max_gain = max(profit_loss_change)
max_loss = min(profit_loss_change)

## This variable will index to the month in which maximum increase and decrease occurred
month_for_max = profit_loss_change.index(max_gain)
month_for_loss = profit_loss_change.index(max_loss)

## The above variables provide the indext number, however, we need the actual months in which these max
# and losses occurred

month_max_index = months_indexing[month_for_max]
month_max_loss_index = months_indexing[month_for_loss]

## Creating a text file to display the data analysis
with open(py_bank_outputfile, 'w') as writedatafile:
    writedatafile.write(f' Financial Analysis\n')
    writedatafile.write(f'-------------------------------------\n')
    writedatafile.write(f'Total Months: {total_months}\n')
    writedatafile.write(f'Total: ${profit_loss_total}\n')
    writedatafile.write(f'Average Change: ${format(average_change,".2f")}\n')
    writedatafile.write(f'Greatest Increase in Profits: {month_max_index} (${format(max_gain,".0f")})\n')
    writedatafile.write(f'Greatest Increase in Profits: {month_max_loss_index} (${format(max_loss,".0f")})\n')
    writedatafile.close()

## Displaying the data analysis onto the terminal
print(f'Financial Analysis')
print(f'-------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${profit_loss_total}')
print(f'Average Change: ${format(average_change,".2f")}')
print(f'Greatest Increase in Profits: {month_max_index} (${format(max_gain,".0f")})')
print(f'Greatest Increase in Profits: {month_max_loss_index} (${format(max_loss,".0f")})')








