def invest(amount, rate, years):
    for i in range(1, years + 1):
        increase = amount * rate / 100
        amount = amount + increase
        print(f'year {i}: ${amount:.2f}')

amount1 = int(input("Please enter how much you want to invest: $"))
rate1 = int(input("Please enter the percentage rate (Just a num is enought!): "))
years1 = int(input("Please enter for how many years you plan to invest: "))

invest(amount1,rate1,years1)