"""bal"""
def paying_debt_offinayear(balance, a_i_r, monthlypaymentrate):
    """payment"""
    temp_b = balance
    no_of_months = 12
    while no_of_months >= 1:
        m_i_r = a_i_r / 12.0
        m_m_p = monthlypaymentrate * temp_b
        m_u_b = temp_b - m_m_p
        u_b_e_m = m_u_b + (m_u_b * m_i_r)
        temp_b = u_b_e_m
        no_of_months -= 1
    return round(temp_b, 2)
def main():
    """balance"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:", paying_debt_offinayear(data[0], data[1], data[2]))
if __name__ == "__main__":
    main()
