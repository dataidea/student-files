calculateAge = lambda birth_year, current_year: current_year - birth_year

def netIncome(income, paye, nssf, tax, heath):
    paye = (paye / 100) * income
    nssf = (nssf / 100) * income
    tax = (tax / 100) * income
    heath = (heath / 100) * income

    net_income = income - paye - nssf - tax - heath
    return net_income


net = netIncome(income=5000000, paye=10, nssf=5, tax=20, heath=5)

print(net)