def invest(amount, rate, years):
    for n in range(1, years +1):
        amount += amount * rate
        print(f"Year {n}: ${amount:.2f}")

dollars = int(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return: "))/100
n_years = int(input("Enter the number of years: "))

invest(dollars, annual_rate, n_years)