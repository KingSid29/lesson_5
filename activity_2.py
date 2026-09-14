actual_cost = float(input("Enter the actual cost"))
sales_amount_cost = float(input("Enter the sales amount"))
if sales_amount_cost > actual_cost:
    profit = sales_amount_cost - actual_cost
    print(f"your profit is £{profit}")
else:
    print("no profit")