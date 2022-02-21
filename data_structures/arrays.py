# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
#     1. In Feb, how many dollars you spent extra compare to January?
#     2. Find out your total expense in first quarter (first three months) of the year.
#     3. Find out if you spent exactly 2000 dollars in any month
#     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#     5. You returned an item that you bought in a month of April and
#     got a refund of 200$. Make a correction to your monthly expense list

monthly_expense = [2200, 2350, 2600, 2130, 2190]

# question 1
answer1 = monthly_expense[2] - monthly_expense[1]
print("Question one is ", answer1)


# question 2
answer2 = monthly_expense[0] + monthly_expense[1] + monthly_expense[2]
print("Question two is", answer2)

# question 3
for expense in monthly_expense:
    if expense == 2000:
        print("You spent 2000 in one month")
        break
    else:
        print("You didn't")
        break

# question 4
june = 1980
monthly_expense.append(june)
print("june added successfully")

# question 5
new_april = monthly_expense[3] - 200
monthly_expense.insert(3, new_april)
print(monthly_expense)
