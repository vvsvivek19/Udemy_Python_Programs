def net_sal(basic, allowance, deductions):
    print('Basic:', basic)
    print('Allowance:', allowance)
    print('Deductions: ', deductions)
    net = basic + allowance - deductions
    return net


n = net_sal(deductions=2000, basic=8000, allowance=6000)
print(n)
