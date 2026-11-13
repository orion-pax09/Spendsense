import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("spendsense_expenses.csv")
#Inspecting dataset condition
print("Display top 10: ")
print(df.head(5))
print("-----------------------------------------")
print("Display last 10: ")
print(df.tail(5))
print("-----------------------------------------")
print("Display shaep: ")
print(df.shape)
print("-----------------------------------------")
print("DF.Columns: ")
print(df.columns)
print("-----------------------------------------")
print("Info: ")
print(df.info())
print("-----------------------------------------")
print("total missing value")
print(df.isnull().sum())
print("-----------------------------------------")
print("total duplicated")
print(df.duplicated().sum())
#filtering row above 1000 amount
cleaned_df = df.copy()
above_1000= cleaned_df[cleaned_df["Amount"]>1000]
print("Above 1000 amount: ")
print(above_1000)
print("------------------------------------------------")
#Find all transactions where:
#1. Category is "Food".
#2. Amount is greater than 500.
filt_food = cleaned_df[(cleaned_df["Category"]=='Food')&(cleaned_df["Amount"]>500)]
print("Only food Category: ")
print(filt_food)
print("===============================================")
#Find all transactions where:
#- Category is "Shopping" OR
#- Amount is greater than 3000.
filt_Shopping = cleaned_df[(cleaned_df["Category"]=="Shopping")|(cleaned_df["Amount"]>3000)]
print("Only Shopping category: ")
print(filt_Shopping)
print("================================================")
#Find all transactions where the payment method is Cash.
filt_cash = cleaned_df[cleaned_df["Payment"]=="Cash"]
print("Only Cash Payment: ")
print(filt_cash)
print("================================================")
#Find the 10 most expensive transactions
expensive = cleaned_df.sort_values(by="Amount" , ascending=False).head(10)
print("Top 10 expensive: ")
print(expensive)
print("================================================")
#Find the 5 cheapest transactions
cheapest = cleaned_df.sort_values(by="Amount" , ascending=True).head(5)
print("Top 5 Cheapest: ")
print(cheapest)
print("================================================")
#Calculate the total Amount spent in each Category.
total = cleaned_df.groupby("Category")["Amount"].sum()
print("Total: ")
print(total)
print("================================================")
#Calculate the average Amount spent in each Category.
avg = cleaned_df.groupby(by="Category")["Amount"].mean()
print("Average: ",avg)
print("================================================")
#Count transactions per payment method
count = cleaned_df.groupby(by="Payment")["Amount"].count()
print("Count: ")
print(count)
print("================================================")
#Find the category with the highest spending
maxval = total.max()
Idxmax= total.idxmax()
print("Highest spending: $",maxval)
print("category: ",Idxmax)
print("================================================")
#Calculate the total spending for each month.
cleaned_df["Date"] = pd.to_datetime(cleaned_df["Date"])
cleaned_df["Month"] = cleaned_df["Date"].dt.month
total_date = cleaned_df.groupby(by="Month")["Amount"].sum()
print(total_date)
#Convert this Python list into a NumPy array called expense_array
numpy_Array = cleaned_df["Amount"].to_numpy()
#Using numpy_Array, calculate:
#1. Total expenses.
#2. Average expense.
#3. Maximum expense.
#4. Minimum expense.
#5. Standard deviation.
#6. Median expenses
total_expenses = np.sum(numpy_Array)
print("Total expenses")
print(total_expenses)
print("================================")
avg_np = np.mean(numpy_Array)
print("Mean expenses")
print(avg_np)
maximum = np.max(numpy_Array)
print("MAximum: ", maximum)
print("================================")
minimum = np.min(numpy_Array)
print("Minimum: " , minimum)
print("================================")
Std = np.std(numpy_Array)
print("Standard Deviation: ", Std)
print("================================")
median_np = np.median(numpy_Array)
print("Median expenses")
print(median_np)
print("================================")
#Find all expenses greater than 1000.
expenses_1000 = numpy_Array[numpy_Array>1000]
print("Expenses greater than 100")
print(expenses_1000)
print("================================")
#Task 2: Find all expenses less than 5000
expenses_5000 = numpy_Array[numpy_Array < 5000]
print("all expenses less than 5000")
print(expenses_5000)
print("================================")
#Find all expenses between 5000 and 200000 (inclusive)
expenses_5000_20000 = numpy_Array[(numpy_Array>=5000) & (numpy_Array <= 200000)]
print("all expenses between 5000 and 200000 (inclusive)")
print(expenses_5000_20000)
print("================================")
# 1. Sort expenses in ascending order
sort_np = np.sort(numpy_Array)
print("expenses in ascending order using numpy")
print(sort_np)
print("================================")
# 2. Sort expenses in descending order
sort_np_desc = np.sort(numpy_Array)[::-1]
print("expenses in descending order")
print(sort_np_desc)
# 3. Find unique expense amounts
unique_np = np.unique(numpy_Array)
print("unique expense amounts")
print(unique_np)
#Challenge 1:
#Using numpy_Array, calculate:
#1. How many transactions are above 2000?
#2. What is the total amount of those transactions?
#3. What is their average amount?

transaction_Above2000 = np.sum(numpy_Array>=2000)
total_Above_2000 = np.sum(numpy_Array[numpy_Array >=2000])
avg_amount = np.mean(numpy_Array[numpy_Array >=2000])
print("Count transactiona above 2000: ",transaction_Above2000)
print("total amount: ",total_Above_2000)
print("average amount: ",avg_amount)
plt.plot(total_date.index,total_date.values,marker="o" , color = "purple")
plt.ylabel("Monthly label")
plt.xlabel("Month")
plt.grid()
plt.title("Monthly expenses")
plt.show()

plt.bar(total.index , total.values , color = "black" , linewidth = 1 , linestyle = "dashed")
plt.grid()
plt.xlabel("Category")
plt.ylabel("Total Amount (PKR)")
plt.title("Total expenses by Categpyory")
plt.show()

plt.pie(total.values , labels=total.index)
plt.title("Expense Distribution by category")
plt.show()