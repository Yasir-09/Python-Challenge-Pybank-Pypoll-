import os
import csv 
#working directory

csvpath=os.path.join('..','Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    month = []
    amount = []
    amount_change = []
    monthly_changes = []
    
    print(f"Header: {csv_header}")               

#Months       
    for row in csvreader:
        month.append(row[0])
        amount.append(row[1])
    print(len(month))
 
 #Total amount 
    amount_int = map(int,amount)
    total_amount = (sum(amount_int))
    print(total_amount)

 #Average Change
    i = 0
    for i in range(len(amount) - 1):
        profit_loss = int(amount[i+1]) - int(amount[i])
 # calculating profit_loss
        amount_change.append(profit_loss)
    Total = sum(amount_change)
    
    #print(amount_change)
    monthly_changes = Total / len(amount_change)
    print(amount_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(amount_change)
    print(profit_increase)
    k = amount_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(amount_change)
    print(profit_decrease)
    j = amount_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print all results

print(f'Financial Analysis'+'\n')

print(f'----------------------------'+'\n')

print("Total Months: " + str(len(month)))

print("Total: $ " + str(total_amount))
      
print("Average Change: $" + str(monthly_changes))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

with open('financal_analysis.txt', 'w') as f:
    f.write(f'Financial Analysis'+'\n')
    f.write("-"*20)
    f.write(f'\n')
    f.write("Total months: " + str(len(month)))
    f.write(f'\n')
    f.write("Total: $ " + str(total_amount))
    f.write(f'\n')
    f.write("Average Change: $" + str(monthly_changes))
    f.write(f'\n')
    f.write(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
    f.write(f'\n')
    f.write(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
