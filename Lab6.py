## David Zheng
## Lab 6
## March 16, 2017

## Target
## r = 0.065
## deposit = 11,000
## target = 100,000
## < 8

def InvestTarget(target, deposit, rate):
    years = 0
    newBalance = deposit
    while newBalance <= target:
        years = years + 1
        print("Year: %d" %years)
        print("Initial Balance: $%.2f" %newBalance)
        newBalance = deposit + newBalance*(1+rate)
        print("Interest: %.3f" %rate)
        print("Deposit: $%.2f" %deposit)
        print("End Balance: $%.2f" %newBalance)

    
    return years

e = InvestTarget(100000, 11000, 0.065)

def InvestYears(years, deposit, rate):
    balance = deposit
    for year in range(1, years + 1):
        balance = deposit + balance*(1+rate)
        print("Year: %d" %year)
        print("Interest: %.3f" %rate)
        print("Deposit: $%.2f" %deposit)
        print("End Balance: $%.2f" %balance)
##    balance = deposit*((1+rate)**years)
##    print("New Balance at %d years is $%.2f" (%years,%balance))

    return balance

#f = InvestYears(30, 11000, 0.065)
