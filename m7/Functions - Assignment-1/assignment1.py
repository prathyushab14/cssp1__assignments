"""bal"""
def payingDebtOffInAYear(balance, annualInterestRate, monthlyPaymentRate):
    """payment"""
    temp_b = balance
    no_of_months = 12
    while no_of_months >= 1:
        monthly_interest_rate = annualInterestRate / 12.0
        minimum_monthly_payment = monthlyPaymentRate * temp_b
        monthly_unpaid_balance = temp_b - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance + (monthly_unpaid_balance * monthly_interest_rate)
        temp_b = updated_balance_each_month
        no_of_months -= 1
    return(round(temp_b, 2))
def main():
    """balance"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:",payingDebtOffInAYear(data[0],data[1],data[2]))
if __name__ == "__main__":
    main()
