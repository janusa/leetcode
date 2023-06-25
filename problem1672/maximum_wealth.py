def maximum_wealth(accounts):
    maximum_customer_wealth = 0
    for customer in accounts:
        customer_wealth = sum(customer)
        maximum_customer_wealth = max(maximum_customer_wealth, customer_wealth)
    return maximum_customer_wealth


print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
