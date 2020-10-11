def trimPaymentsGraph(payments):
    index = -1
    if type(payments) == list:
        for i in range(len(payments)):
            if payments[i].get('balanceOut') <= 0:
                index = i
                break
    
    if index >= 0 and index < len(payments) - 1:
        payments = payments[:index + 1]
        payments[index]['payment'] = payments[index]['debt']

    return payments