import numpy_financial as npf

# Coupon payment per period
coupon_payment = 5
# Time to maturity in periods
maturity = 5
# Face value of the bond
face_value = 100
# Discount rate
discount_rate = 0.05

cash_flows = [coupon_payment] * maturity
cash_flows[-1] += face_value

print(cash_flows)

bond_price = npf.npv(discount_rate, cash_flows)

print("Bond Price: {:.2f}".format(bond_price))
