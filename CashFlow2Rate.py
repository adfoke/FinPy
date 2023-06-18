import numpy_financial as npf


# base on the cash_flows calc the real rate

#firt 3 year pay 100000, last 3 year get 110000
cash_flows = [-100000, -100000, -100000, 110000, 110000, 110000]

#get 100000 in 1 year, pay 35000 in 4 year
cash_flows2 = [100000,-35000,-35000,-35000,-35000]

irr = npf.irr(cash_flows)
print("Annual Rate: {:.2%}".format(irr))
irr2 = npf.irr(cash_flows2)
print("Annual Rate: {:.2%}".format(irr2))
